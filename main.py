import os
import sys
import time
import threading
import subprocess
from pathlib import Path

# Thêm thư viện giao diện Console
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TaskProgressColumn
)

# Khởi tạo Console của rich
console = Console()

# Thêm thư mục hiện tại vào sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Bật mã màu ANSI trên Windows CMD / Terminal
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')

# 1. Import các module xử lý APK
from decmhl.apk_api import ApkApi

# 2. Import các module của Smali Reader Pro
from apimhl.scanner import scan_smali
from apimhl.merger import merge_classes
from apimhl.translator import translate_groups
from apimhl.formatter import format_groups
from apimhl.writer import (
    write_output,
    write_merged,
    export_statistics
)
from apimhl.config import (
    output_path,
    EXPORT_MERGED_FILE,
    EXPORT_STATISTICS
)

# Bảng mã màu ANSI
C_RESET   = "\033[0m"
C_BOLD    = "\033[1m"
C_CYAN    = "\033[96m"
C_GREEN   = "\033[92m"
C_YELLOW  = "\033[93m"
C_RED     = "\033[91m"
C_MAGENTA = "\033[95m"
C_BLUE    = "\033[94m"

def clean_path(path_input: str) -> str:
    """Xóa dấu nháy khi kéo thả file/folder vào Terminal"""
    return path_input.strip().strip('"').strip("'")

def print_banner():
    print(f"""{C_CYAN}{C_BOLD}
 ███╗   ███╗████████╗██████╗  ██████╗ ██╗
 ████╗ ████║╚══██╔══╝██╔══██╗██╔═══██╗██║
 ██╔████╔██║   ██║   ██║  ██║██║   ██║██║
 ██║╚██╔╝██║   ██║   ██║  ██║██║   ██║██║
 ██║ ╚═╝ ██║   ██║   ██████╔╝╚██████╔╝███████╗
 ╚═╝     ╚═╝   ╚═╝   ╚═════╝  ╚══════╝ ╚══════╝{C_RESET}
{C_MAGENTA}{C_BOLD}► UNIFIED TOOL: APK DECOMPILER & SMALI READER PRO ◄{C_RESET}
""")

def print_menu():
    print_banner()
    print(f"""{C_BLUE}╔══════════════════════════════════════════════════════════════╗
║                   {C_BOLD}{C_CYAN}BẢNG ĐIỀU KHIỂN CHÍNH{C_RESET}{C_BLUE}                   ║
╠══════════════════════════════════════════════════════════════╣
║  {C_GREEN}[1]{C_RESET} 🔓  {C_BOLD}GIẢI NÉN APK & TỰ ĐỘNG CHẠY SMALI READER PRO{C_RESET}     ║
║  {C_GREEN}[2]{C_RESET} 📜  {C_BOLD}CHỈ CHẠY SMALI READER PRO{C_RESET} (Chọn thư mục thủ công)  ║
║  {C_GREEN}[3]{C_RESET} 📦  {C_BOLD}ĐÓNG GÓI MULTI-DEX{C_RESET} (Từ thư mục Smali)           ║
║  {C_RED}[0]{C_RESET} ❌  {C_BOLD}THOÁT{C_RESET}     : Thoát chương trình                     ║
╚══════════════════════════════════════════════════════════════╝{C_RESET}
""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# =====================================================================
# HÀM HỖ TRỢ: CHẠY THANH TIẾN TRÌNH VÀ BẮT BUỘC CHẶN MỌI LOG RÁC (AN TOÀN)
# =====================================================================
def run_with_progress(description: str, func, *args, **kwargs):
    """
    Chạy một hàm Python trên thread riêng và hiển thị thanh tiến trình rich,
    đồng thời chặn log rác mà không làm gián đoạn luồng pipe của subprocess.
    """
    result = [None]
    exception = [None]

    orig_popen = subprocess.Popen
    orig_system = os.system

    def silent_popen(*p_args, **p_kwargs):
        # Chỉ ẩn nếu tiến trình không chủ động tạo pipe truyền dữ liệu
        if p_kwargs.get('stdout') is None:
            p_kwargs['stdout'] = subprocess.DEVNULL
        if p_kwargs.get('stderr') is None:
            p_kwargs['stderr'] = subprocess.DEVNULL
        return orig_popen(*p_args, **p_kwargs)

    def silent_system(command):
        hide_suffix = " > nul 2>&1" if sys.platform == 'win32' else " > /dev/null 2>&1"
        return orig_system(str(command) + hide_suffix)

    def target():
        # Ép chế độ ẩn log an toàn
        subprocess.Popen = silent_popen
        os.system = silent_system
        try:
            result[0] = func(*args, **kwargs)
        except Exception as e:
            exception[0] = e
        finally:
            # Khôi phục hàm gốc
            subprocess.Popen = orig_popen
            os.system = orig_system

    thread = threading.Thread(target=target)
    thread.start()

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=40, complete_style="green"),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task(description, total=100)
        current = 0
        
        while thread.is_alive():
            if current < 95:
                current += 1
                progress.update(task, completed=current)
            time.sleep(0.1)
            
        progress.update(task, completed=100)

    if exception[0]:
        raise exception[0]
    return result[0]

# =====================================================================
# CHỨC NĂNG SMALI READER PRO
# =====================================================================
def run_smali_reader(folder: str):
    print(f"\n{C_CYAN}{C_BOLD}───► BẮT ĐẦU QUÉT VÀ XỬ LÝ SMALI TỪNG THƯ MỤC RIÊNG BIỆT{C_RESET}")
    
    if not os.path.isdir(folder):
        print(f"\n{C_RED}[ERROR] Không tìm thấy thư mục: {folder}{C_RESET}")
        return

    subfolders = []
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path) and (item == "smali" or item.startswith("smali_")):
            subfolders.append(item_path)
    
    subfolders.sort()

    if not subfolders:
        subfolders = [folder]

    print(f"\n{C_YELLOW}[i] Tìm thấy {len(subfolders)} thư mục smali cần xử lý riêng.{C_RESET}")

    for idx, sub_dir in enumerate(subfolders, 1):
        folder_name = os.path.basename(sub_dir)
        print(f"\n" + "─" * 60)
        print(f"{C_BOLD}[Thư mục {idx}/{len(subfolders)}] Đang xử lý: {C_GREEN}{folder_name}{C_RESET}")
        
        console.print("[yellow][1/4] Đang quét file...[/yellow]")
        files = scan_smali(sub_dir)
        if len(files) == 0:
            console.print(f"[red]Không tìm thấy file .smali nào trong {folder_name}, bỏ qua.[/red]")
            continue
            
        console.print("[yellow][2/4] Đang gom nhóm dữ liệu...[/yellow]")
        groups = merge_classes(files)
        
        processed_groups = {}
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan][3/4] Đang chuyển đổi và định dạng ({task.completed}/{task.total})"),
            BarColumn(bar_width=40),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Processing", total=len(groups))
            
            for key, value in groups.items():
                try:
                    single_translated = translate_groups({key: value})
                    single_formatted = format_groups(single_translated)
                    processed_groups.update(single_formatted)
                except Exception as e:
                    console.print(f"[red]Lỗi chuyển đổi ({key}): {e}[/red]")
                
                progress.update(task, advance=1)

        output = output_path(sub_dir)
        console.print(f"[yellow][4/4] Đang ghi file cho {folder_name}...[/yellow]")
        write_output(output, processed_groups)

        if EXPORT_MERGED_FILE:
            write_merged(output, processed_groups)

        if EXPORT_STATISTICS:
            export_statistics(output, processed_groups)

        print(f"{C_GREEN}[✔] Hoàn thành {folder_name}! Đầu ra tại: {output}{C_RESET}")

    print("\n" + "=" * 60)
    print(f"{C_GREEN}[✔] Đã xử lý xong tất cả các thư mục Smali!{C_RESET}")
    print("=" * 60)

# =====================================================================
# CHỨC NĂNG ĐÓNG GÓI MULTI-DEX
# =====================================================================
def run_build_dex(apimhl, root_dir: str):
    print(f"\n{C_CYAN}{C_BOLD}───► ĐANG TIẾN HÀNH ĐÓNG GÓI MULTI-DEX{C_RESET}")
    out_dex_dir = os.path.join(root_dir, "output_dex")
    
    print(f"{C_YELLOW}[*] Thư mục nguồn: {root_dir}{C_RESET}")
    print(f"{C_YELLOW}[*] Thư mục xuất file .DEX: {out_dex_dir}{C_RESET}\n")

    results = run_with_progress("[*] TIẾN TRÌNH: Đang đóng gói file DEX...", apimhl.build_all_dex, root_dir=root_dir, output_dir=out_dex_dir)

    if results:
        print(f"\n{C_GREEN}[✔] Đóng gói thành công! Lưu tại: {out_dex_dir}{C_RESET}")
    else:
        print(f"\n{C_RED}[-] Đóng gói thất bại!{C_RESET}")

# =====================================================================
# HÀM MAIN CHÍNH
# =====================================================================
def main():
    try:
        apimhl = ApkApi()
    except Exception as e:
        print(f"{C_RED}[-] Lỗi khởi tạo ApkApi: {e}{C_RESET}")
        input("\nNhấn Enter để thoát...")
        return

    while True:
        clear_screen()
        print_menu()
        choice = input(f"{C_YELLOW}👉 Chọn chức năng (0-3): {C_RESET}").strip()

        if choice == "1":
            print(f"\n{C_CYAN}{C_BOLD}───► CHỨC NĂNG 1: GIẢI NÉN APK & ĐỌC SMALI{C_RESET}")
            apk_path = clean_path(input(f"{C_YELLOW}[?] Kéo thả file .APK vào đây: {C_RESET}"))
            
            if not os.path.isfile(apk_path):
                print(f"{C_RED}[-] File không tồn tại: {apk_path}{C_RESET}")
                input("\nNhấn Enter để tiếp tục...")
                continue

            out_dir = clean_path(input(f"{C_YELLOW}[?] Thư mục đầu ra (Enter để dùng mặc định): {C_RESET}"))
            if not out_dir:
                out_dir = os.path.splitext(apk_path)[0] + "_out"
            print("")
            
            is_success = run_with_progress("[*] TIẾN TRÌNH: Đang giải nén APK...", apimhl.decompile, apk_path=apk_path, output_dir=out_dir)

            if is_success:
                print(f"\n{C_GREEN}[✔] Giải nén thành công tại: {out_dir}{C_RESET}")
                run_smali_reader(out_dir)
            else:
                print(f"\n{C_RED}[-] Giải nén thất bại!{C_RESET}")

            input("\nNhấn Enter để quay lại menu...")

        elif choice == "2":
            print(f"\n{C_CYAN}{C_BOLD}───► CHỨC NĂNG 2: CHẠY SMALI READER PRO{C_RESET}")
            folder = clean_path(input(f"{C_YELLOW}[?] Nhập hoặc kéo thả thư mục chứa Smali: {C_RESET}"))
            run_smali_reader(folder)
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "3":
            print(f"\n{C_CYAN}{C_BOLD}───► CHỨC NĂNG 3: ĐÓNG GÓI MULTI-DEX{C_RESET}")
            root_dir = clean_path(input(f"{C_YELLOW}[?] Kéo thả THƯ MỤC CHA chứa mã Smali: {C_RESET}"))
            
            if not os.path.isdir(root_dir):
                print(f"{C_RED}[-] Thư mục không tồn tại: {root_dir}{C_RESET}")
                input("\nNhấn Enter để tiếp tục...")
                continue

            run_build_dex(apimhl, root_dir)
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "0":
            print(f"\n{C_GREEN}[*] Cảm ơn bạn đã sử dụng tool!{C_RESET}")
            break
        else:
            print(f"{C_RED}[-] Lựa chọn không hợp lệ!{C_RESET}")
            input("\nNhấn Enter để thử lại...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nĐã hủy.")
    except Exception as e:
        print(f"\n[LỖI NGHIÊM TRỌNG]: {e}")
        input("\nNhấn Enter để thoát...")