import os
from services.color import Color
import shutil
from API.golike import GOLIKE
from API.pinterest import Pinterest
from API.instagram import INSTAGRAM
from API.threads import Thread
from API.linkedin import Linkedin
from API.bluesky import BlueSky
import API.youtube as YT
from config.configpy import *
import requests
import platform
from time import sleep
import sys
import services.services as sr
import services.adb as adb
import dns.resolver
resolver = dns.resolver.Resolver()
resolver.nameservers = ["1.1.1.1"]
def ascii_img():
        print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")     
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  ")
        print(Color.CYAN+f"[*-*] {Color.LIGHT_WHITE}=> {Color.RED}DISCORD : {Color .LIGHT_GREEN}MINHHOALONG6 "+ Color.END)                                                  
   
def draw_full_width_box_mini(text):
    terminal_width = shutil.get_terminal_size().columns // 3 
    text_with_color = Color.YELLOW + text + Color.GREEN
    text_len = len(text)
    padding_total = terminal_width - 2 - text_len
    padding_left = padding_total // 2
    padding_right = padding_total - padding_left
    print(Color.GREEN + "┌" + "─" * (terminal_width - 2) + "┐")
    print("│" + " " * padding_left + text_with_color + " " * padding_right + "│")
    print("└" + "─" * (terminal_width - 2) + "┘" + Color.END)
def draw_full_width_box(text):
    terminal_width = shutil.get_terminal_size().columns
    text_with_color = Color.YELLOW + text + Color.GREEN
    text_len = len(text)
    padding_total = terminal_width - 2 - text_len
    padding_left = padding_total // 2
    padding_right = padding_total - padding_left
    print(Color.GREEN + "┌" + "─" * (terminal_width - 2) + "┐")
    print("│" + " " * padding_left + text_with_color + " " * padding_right + "│")
    print("└" + "─" * (terminal_width - 2) + "┘" + Color.END)
def split_terminal():
    width = os.get_terminal_size().columns
    print("-" * width)
def LOGO_TEXT(text1,text2):
    print(f"{Color.RED}[{Color.END}:D{Color.RED}]{Color.END} => {Color.GREEN} {text1} : {Color.CYAN} {text2} {Color.END}")
def FN_TEXT(int_id,text2):
    print(f"{Color.RED}[{Color.END}θ{Color.RED}]{Color.END}{chr(172)}{Color.GREEN} {Color.YELLOW}{int_id}{Color.END} => {Color.CYAN}{text2}{Color.END}")
def warning_text(text1):
    print(f"{Color.RED}[{Color.END}!{Color.RED}]{Color.END} => {Color.GREEN} {text1} ")
def input_text(text1):
    data = input(f"{Color.RED}[{Color.END}＄{Color.RED}]{Color.END} => {Color.GREEN} {text1} {Color.END}")
    return data
def choose_input(text):
    data = input(f"{Color.RED}[{Color.END}I{Color.RED}]{Color.END} => {Color.GREEN} {text} {Color.END}")
    return data
def MENU_FN(choose):
    print()
def menu_live(info,auth):
    split_terminal()
    LOGO_TEXT("ID Tài Khoản",str(info["data"]["id"]))
    LOGO_TEXT("Tên Người Dùng",str(info["data"]["name"]))
    LOGO_TEXT("Tên Tài Khoản",str(info["data"]["username"]))
    LOGO_TEXT("Số dư",str(info["data"]["coin"]))
    split_terminal()
    draw_full_width_box("THÔNG TIN THIẾT BỊ")
    LOGO_TEXT("Hệ điều hành hành",str(platform.system()))
    try:
        info_ip = requests.get("http://ip-api.com/json")
        if(info_ip.status_code == 200):
            LOGO_TEXT("IP",str(info_ip.json()['query']))
            LOGO_TEXT("Khu Vực",str(info_ip.json()['regionName']))
            LOGO_TEXT("Isp",str(info_ip.json()['isp']))
            LOGO_TEXT("Nhà Mạng",str(info_ip.json()['org']))
        else:
            LOGO_TEXT("IP","Không xác định")
            LOGO_TEXT("Khu Vực","Không xác định")
            LOGO_TEXT("Isp","Không xác định")
            LOGO_TEXT("Nhà Mạng","Không xác định")
    except KeyboardInterrupt:
                    sys.exit(0)
    except:
        LOGO_TEXT("IP","Không xác định")
        LOGO_TEXT("Khu Vực","Không xác định")
        LOGO_TEXT("Isp","Không xác định")
        LOGO_TEXT("Nhà Mạng","Không xác định")
    split_terminal()
    draw_full_width_box("CHỨC NĂNG GOLIKE")    
    draw_full_width_box_mini("REQUESTS => [PC+MOBILE]") 
    FN_TEXT(1,"Chạy Tự Động Instagram")
    FN_TEXT(2,"Chạy Tự Động Threads")
    FN_TEXT(3,"Chạy Tự Động Linkedin")
    FN_TEXT(4,"Chạy Tự Động Pinterest")
    FN_TEXT(16,"Chạy Tự Động Youtube")
    FN_TEXT(17,"Chạy Tự Động BlueSky")
    draw_full_width_box_mini("AUTO CLICK(MOBILE UBUNTU)")
    FN_TEXT(5,"Chạy Tự Động TikTok(KHÔNG DÙNG ADB BUỘC DÙNG AUTO CLICK)")
    FN_TEXT(13,"Chạy Tự Động TikTokStudio(KHÔNG DÙNG ADB BUỘC DÙNG AUTO CLICK)")
    FN_TEXT(14,"Chạy Tự Động TikTokLite(KHÔNG DÙNG ADB BUỘC DÙNG AUTO CLICK)")
    draw_full_width_box_mini("ADB => [MOBILE Hoặc PC Cắm USB-CAP]") 
    FN_TEXT(6,"Chạy Tự Động TikTok(Tự Động Lấy Tọa Độ)")
    FN_TEXT(7,"Chạy Tự Động TikTok Studio(Tự Động Lấy Tọa Độ)")
    FN_TEXT(8,"Chạy Tự Động TikTok Lite(Tự Động Lấy Tọa Độ)")
    FN_TEXT(9,"Chạy Tự Động TikTok(Lấy Tọa Độ Thủ Công)")
    FN_TEXT(10,"Chạy Tự Động TikTok US(Tự Động Lấy Tọa Độ)")
    FN_TEXT(15,"Chạy Tự Động Snapchat(Tự Động Lấy Tọa Độ)")
    draw_full_width_box_mini("ADB + AUTOCLICK")
    FN_TEXT(11,"Chạy Tự Động TikTok US(AUTOCLICK)")
    FN_TEXT(12,"Chạy Tự Động TikTok Studio(AUTOCLICK)")
    draw_full_width_box("ĐỔI Authorization") 
    FN_TEXT(0,"ĐỔI Authorization")
    while True:
        try:
            CHOOSE = choose_input("NHẬP CHỨC NĂNG CỦA TOOL : ")
            if int(CHOOSE) >= 0 and int(CHOOSE) <= 17:
                break
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass
    if CHOOSE == "6":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            rlm = input_text("Chạy Với RL_Mode(Y/N) : ")
            if(rlm.lower()=="y" or rlm.lower() == "n"):
                break
        if rlm.lower()=="y":
            while True:
                try:
                    rlm_idx = input_text("Sau ? Nhiệm vụ chạy RL_Mode(Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                    if "," in rlm_idx:
                        rlm_idx = rlm_idx.split(",")
                        rlm_idx = [int(x) for x in rlm_idx]
                        if(rlm_idx[0]<rlm_idx[1] and min(rlm_idx) != 0):
                            rlm_idx = random.randint(rlm_idx[0],rlm_idx[1])
                            break
                    else:
                        if int(rlm_idx) > 0:
                            break
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e :
                    pass
            while True:
                try:
                    rlm_time = input_text("Thời Gian RL_Mode : ")
                    if int(rlm_time) > 0:
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e :
                    pass      
            LOGO_TEXT(f"Sau ? thì sẽ chạy RL_MODE ! ",int(rlm_idx))
            while True:
                    rlm_delay = input_text("Delay Giữa Các Hành Động : ")
                    if int(rlm_delay) >0 : break
        else:
            rlm_time = 0
            rlm_idx = 0
            while True:
                try:
                    rlm_delay = input_text("Delay Giữa Các Hành Động : ")
                    if int(rlm_delay) >0 : break  
                except KeyboardInterrupt:
                    sys.exit(0)    
                except Exception as e:
                    pass
        while True:
            try:
                CHECK_NHA = input_text("Reload Check Nhả(Y/N) : ")
                if CHECK_NHA.upper() == "Y" or CHECK_NHA.upper() == "N":
                     break
            except KeyboardInterrupt:
                sys.exit(0)    
            except Exception as e:
                pass
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass   
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK(device,auth,account[1][int(account_id)-1],int(rlm_idx),delay_min,delay_max,int(rlm_delay),CHECK_NHA,NV_fail,rlm_time)
    elif CHOOSE == "15":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("snapchat","name")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try:
                rlm_delay = input_text("Delay Giữa Các Hành Động : ")
                if int(rlm_delay) >0 : break  
            except KeyboardInterrupt:
                sys.exit(0)    
            except Exception as e:
                pass
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.SNAPCHAT(device,auth,account[1][int(account_id)-1],delay_min,delay_max,int(rlm_delay))
    elif CHOOSE =="10":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try:
                rlm_delay = input_text("Delay Giữa Các Hành Động : ")
                if int(rlm_delay) >0 : break  
            except KeyboardInterrupt:
                sys.exit(0)    
            except Exception as e:
                pass
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass      
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK_US(device,auth,account[1][int(account_id)-1],delay_min,delay_max,int(rlm_delay),NV_fail)
    elif CHOOSE =="11":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
       
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass      
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK_AUTOCLICK_US_ADB(device,auth,account[1][int(account_id)-1],delay_min,delay_max,NV_fail)
    elif CHOOSE =="12":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
       
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass      
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK_AUTOCLICK_TIKTOKSTUDIO_ADB(device,auth,account[1][int(account_id)-1],delay_min,delay_max,NV_fail)
    elif CHOOSE=="7":
        nickname_list = []
        account_id_list_ = []
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if ',' in account_id:
                    for i in account_id.split(','):
                        nickname_list.append(account[2][int(i)-1])
                        account_id_list_.append(account[1][int(i)-1])
                    break
                   
                else:
                    if(int(account_id)>0 and int(account_id)<=len(account[1])):
                        nickname_list.append(account[2][int(account_id)-1])
                        account_id_list_.append(account[1][int(account_id)-1])
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try:
                rlm_delay = input_text("Delay Giữa Các Hành Động : ")
                if int(rlm_delay) >0 : break  
            except KeyboardInterrupt:
                sys.exit(0)    
            except Exception as e:
                pass
        while True:
            try:
                CHECK_NHA = input_text("Reload Check Nhả(Y/N) : ")
                if CHECK_NHA.upper() == "Y" or CHECK_NHA.upper() == "N":
                     break
            except KeyboardInterrupt:
                sys.exit(0)    
            except Exception as e:
                pass
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        if (len(account_id_list_)>1):
            while True:
                try :
                    delay2 =  int(input_text("Nhập delay chuyển acc (Lưu Ý đây là bản thử nghiệm có thể bị lỗi) : "))
                    if int(delay2) > 0:    
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    pass
            while True:
                try :
                    sonv_chuyenacc =  int(input_text("Sau Bao Nhiêu Nhiệm Vụ Thì Chuyển Acc : "))
                    if int(sonv_chuyenacc) > 0:    
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    pass
            
        else:
            delay2 = 0
            sonv_chuyenacc = 0
        while True:
            try:
                CHECK_NV_1 = input_text("Bỏ qua tài khoản riêng tư (hoặc bị cấm) bằng ADB (Y/N) : ")  
                if CHECK_NV_1.upper() == "Y" or CHECK_NV_1.upper() == "N":
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass 
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK_STUDIO(device,auth,account_id_list_,delay_min,delay_max,int(rlm_delay),CHECK_NHA,NV_fail,CHECK_NV_1,nickname_list,delay2,int(sonv_chuyenacc))
    elif CHOOSE=="8":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try:
                rlm_delay = input_text("Delay Giữa Các Hành Động : ")
                if int(rlm_delay) >0 : break  
            except KeyboardInterrupt:
                sys.exit(0)    
            except Exception as e:
                pass
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass         
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK_LITE(device,auth,account[1][int(account_id)-1],delay_min,delay_max,int(rlm_delay),NV_fail)
    elif CHOOSE == "1":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("instagram","instagram_username")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if ',' in account_id:
                    account_id_list = account_id.split(',')
                    break
                else:
                    if(int(account_id)>0 and int(account_id)<=len(account[1])):
                        account_id_list = [account_id]
                        break
                   
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG") 
        cookieslist = []
        if len(account_id_list) == 1:
            if check_cookies("INSTAGRAM",str(account[1][int(account_id_list[0])-1])) == False:
                while True:
                    try:
                        COOKIES = input_text("Nhập Cookies : ")
                        check = INSTAGRAM(COOKIES).GETINFO()
                        
                        if check != False:
                            ADD_COOKIES("INSTAGRAM",str(account[1][int(account_id_list[0])-1]),COOKIES)
                            break
                    except KeyboardInterrupt:
                        sys.exit(0)
            else:
                    for i in range(1, 4):
                        msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                        clear = " " * (80 - len(msg)) 
                        print(f"\r{msg}{clear}", end="")
                        sys.stdout.flush()
                        sleep(0.5)
                    data = LoadJSON()
                    COOKIES = data['data']['MXH']["INSTAGRAM"]['auth'][str(account[1][int(account_id_list[0])-1])]
                    check = INSTAGRAM(COOKIES).GETINFO()
                    if check != False:
                        print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                    else:
                        print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                        data['data']['MXH']["INSTAGRAM"]['auth'][str(account[1][int(account_id_list[0])-1])] = ""
                        SaveJSON(data)
                        print("\r" + " " * 50 + "\r", end="")
                        while True:
                            try:
                                COOKIES = input_text("Nhập Cookies : ")
                                check = INSTAGRAM(COOKIES).GETINFO()
                                if check != False:
                                    ADD_COOKIES("INSTAGRAM",str(account[1][int(account_id_list[0])-1]),COOKIES)
                                    break
                            except KeyboardInterrupt:
                                sys.exit(0)
            data = LoadJSON()
            cookieslist.append({str(account[1][int(account_id_list[0])-1]):data['data']['MXH']["INSTAGRAM"]['auth'][str(account[1][int(account_id_list[0])-1])]})
        else:
            for j in range(len(account_id_list)): 
                if check_cookies("INSTAGRAM",str(account[1][int(account_id_list[j])-1])) == False:
                    while True:
                        try:
                            COOKIES = input_text(f"Nhập Cookies {Color.GREEN}{str(account[0][int(account_id_list[j])-1])}: ")
                            check = INSTAGRAM(COOKIES).GETINFO()
                            if check != False:
                                ADD_COOKIES("INSTAGRAM",str(account[1][int(account_id_list[j])-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                            sys.exit(0)
                else:
                        for i in range(1, 4):
                            msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                            clear = " " * (80 - len(msg)) 
                            print(f"\r{msg}{clear}", end="")
                            sys.stdout.flush()
                            sleep(0.5)
                        data = LoadJSON()
                        COOKIES = data['data']['MXH']["INSTAGRAM"]['auth'][str(account[1][int(account_id_list[j])-1])]
                        check = INSTAGRAM(COOKIES).GETINFO()
                        if check != False:
                            print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                        else:
                            print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                            data['data']['MXH']["INSTAGRAM"]['auth'][str(account[1][int(account_id_list[j])-1])] = ""
                            SaveJSON(data)
                            print("\r" + " " * 50 + "\r", end="")
                            while True:
                                try:
                                    COOKIES = input_text(f"Nhập Cookies {Color.GREEN}{str(account[0][int(account_id_list[j])-1])}: ")
                                    check = INSTAGRAM(COOKIES).GETINFO()
                                    if check != False:
                                        ADD_COOKIES("INSTAGRAM",str(account[1][int(account_id_list[j])-1]),COOKIES)
                                        break
                                except KeyboardInterrupt:
                                    sys.exit(0)  
                data = LoadJSON()
                cookieslist.append({str(account[1][int(account_id_list[j])-1]):data['data']['MXH']["INSTAGRAM"]['auth'][str(account[1][int(account_id_list[j])-1])]})
            
        while True:
            try:
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  
                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e: 
                pass
        while True:
            try:
                block_idx =  input_text("Sau bao nhiêu nhiệm vụ bị giới hạn thì đổi acc : ")
                if int(block_idx)>0:
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e: 
                pass
        
        draw_full_width_box("ĐANG AUTO")
        sr.instagram(auth,cookieslist,delay_min,delay_max,block_idx)
        
    elif CHOOSE=="2":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("threads","threads_username")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if ',' in account_id:
                    account_id_list = account_id.split(',')
                    break
                else:
                    if(int(account_id)>0 and int(account_id)<=len(account[1])):
                        account_id_list = [account_id]
                        break
                   
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")  
        cookieslist = []
        if len(account_id_list) == 1:
            if check_cookies("THREADS",str(account[1][int(account_id_list[0])-1])) == False:
                    while True:
                        try:
                            COOKIES = input_text("Nhập Cookies : ")
                            check = Thread(COOKIES).GETDATA()
                            if check != False:
                                ADD_COOKIES("THREADS",str(account[1][int(account_id_list[0])-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                            sys.exit(0)
            else:
                    for i in range(1, 4):
                        msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                        clear = " " * (80 - len(msg)) 
                        print(f"\r{msg}{clear}", end="")
                        sys.stdout.flush()
                        sleep(0.5)
                    data = LoadJSON()
                    COOKIES = data['data']['MXH']["THREADS"]['auth'][str(account[1][int(account_id_list[0])-1])]
                    check = Thread(COOKIES).GETDATA()
                    if check != False:
                        print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                    else:
                        print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                        data['data']['MXH']["THREADS"]['auth'][str(account[1][int(account_id_list[0])-1])] = ""
                        SaveJSON(data)
                        print("\r" + " " * 50 + "\r", end="")
                        while True:
                            try:
                                COOKIES = input_text("Nhập Cookies : ")
                                check = Thread(COOKIES).GETDATA()
                                if check != False:
                                    ADD_COOKIES("THREADS",str(account[1][int(account_id_list[0])-1]),COOKIES)
                                    break
                            except KeyboardInterrupt:
                                sys.exit(0)
            data = LoadJSON()
            cookieslist.append({str(account[1][int(account_id_list[0])-1]):data['data']['MXH']["THREADS"]['auth'][str(account[1][int(account_id_list[0])-1])]})
        else:
            for j in range(len(account_id_list)): 
                if check_cookies("THREADS",str(account[1][int(account_id_list[j])-1])) == False:
                    while True:
                        try:
                            COOKIES = input_text(f"Nhập Cookies {Color.GREEN}{str(account[0][int(account_id_list[j])-1])}: ")
                            check = Thread(COOKIES).GETDATA()
                            if check != False:
                                ADD_COOKIES("THREADS",str(account[1][int(account_id_list[j])-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                            sys.exit(0)
                else:
                        for i in range(1, 4):
                            msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                            clear = " " * (80 - len(msg)) 
                            print(f"\r{msg}{clear}", end="")
                            sys.stdout.flush()
                            sleep(0.5)
                        data = LoadJSON()
                        COOKIES = data['data']['MXH']["THREADS"]['auth'][str(account[1][int(account_id_list[j])-1])]
                        check = Thread(COOKIES).GETDATA()
                        if check != False:
                            print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                        else:
                            print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                            data['data']['MXH']["THREADS"]['auth'][str(account[1][int(account_id_list[j])-1])] = ""
                            SaveJSON(data)
                            print("\r" + " " * 50 + "\r", end="")
                            while True:
                                try:
                                    COOKIES = input_text(f"Nhập Cookies {Color.GREEN}{str(account[0][int(account_id_list[j])-1])}: ")
                                    check = Thread(COOKIES).GETDATA()
                                    if check != False:
                                        ADD_COOKIES("THREADS",str(account[1][int(account_id_list[j])-1]),COOKIES)
                                        break
                                except KeyboardInterrupt:
                                    sys.exit(0)  
                data = LoadJSON()
                cookieslist.append({str(account[1][int(account_id_list[j])-1]):data['data']['MXH']["THREADS"]['auth'][str(account[1][int(account_id_list[j])-1])]})
        while True:
            try:
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  
                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        draw_full_width_box("ĐANG AUTO")
        sr.threads(auth,cookieslist,delay_min,delay_max)
    elif CHOOSE == "3":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("linkedin","name")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")  
        if check_cookies("LINKEDIN",str(account[1][int(account_id)-1])) == False:
                while True:
                    try:
                        COOKIES = input_text("Nhập Cookies : ")
                        check = Linkedin(COOKIES).GETDATA()
                        if check != False:
                            ADD_COOKIES("LINKEDIN",str(account[1][int(account_id)-1]),COOKIES)
                            break
                    except KeyboardInterrupt:
                        sys.exit(0)
        else:
                for i in range(1, 4):
                    msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                    clear = " " * (80 - len(msg)) 
                    print(f"\r{msg}{clear}", end="")
                    sys.stdout.flush()
                    sleep(0.5)
                data = LoadJSON()
                COOKIES = data['data']['MXH']["LINKEDIN"]['auth'][str(account[1][int(account_id)-1])]
                check = Linkedin(COOKIES).GETDATA()
                if check != False:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                else:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                    data['data']['MXH']["LINKEDIN"]['auth'][str(account[1][int(account_id)-1])] = ""
                    SaveJSON(data)
                    print("\r" + " " * 50 + "\r", end="")
                    while True:
                        try:
                            COOKIES = input_text("Nhập Cookies : ")
                            check = Linkedin(COOKIES).GETDATA()
                            if check != False:
                                ADD_COOKIES("LINKEDIN",str(account[1][int(account_id)-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                             sys.exit(0)
        while True:
            try:
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  
                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        draw_full_width_box("ĐANG AUTO")
        sr.Linkedin(auth,account[1][int(account_id)-1],COOKIES,delay_min,delay_max)
    elif CHOOSE == "9":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        X = input_text("Nhập Tọa độ X : ")
        Y = input_text("Nhập Tọa độ Y : ")
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass      
        draw_full_width_box("DEVICES")
        devices = adb.adb_conneted()
        if devices != False:
            if(len(devices)==1):
                device = devices[0]
                warning_text("Phát hiện chỉ có một thiết bị tự động chạy defaut ! ")
            else:
                idx = input_text("NHẬP THIẾT BỊ MUỐN CHẠY AUTO : ")
                device = devices[int(idx)-1]
            draw_full_width_box("ĐANG AUTO")
            sr.TIKTOK_XY(device,auth,account[1][int(account_id)-1],delay_min,delay_max,X,Y,NV_fail)
    elif CHOOSE == "5":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass   
        draw_full_width_box("ĐANG AUTO")
        sr.TIKTOK_AUTOCLICK(auth,account[1][int(account_id)-1],delay_min,delay_max,NV_fail)
    elif CHOOSE == "13":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass   
        draw_full_width_box("ĐANG AUTO")
        sr.TIKTOK_studio_AUTOCLICK(auth,account[1][int(account_id)-1],delay_min,delay_max,NV_fail)
    elif CHOOSE == "14":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("tiktok","nickname")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")
        while True:
            try :
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  

                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        while True:
            try :
                NV_fail =  int(input_text("Sau Bao Nhiêu NV Thất Bại Thì Thoát Tool : "))
                if int(NV_fail) >= 0:    
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass   
        draw_full_width_box("ĐANG AUTO")
        sr.TIKTOK_Lite_AUTOCLICK(auth,account[1][int(account_id)-1],delay_min,delay_max,NV_fail)
    elif CHOOSE == "4":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("pinterest","name")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG")  
        if check_cookies("PINTEREST",str(account[1][int(account_id)-1])) == False:
                while True:
                    try:
                        COOKIES = input_text("Nhập Cookies : ")
                        check = Pinterest(COOKIES).GETDATA()
                        if check != False:
                            ADD_COOKIES("PINTEREST",str(account[1][int(account_id)-1]),COOKIES)
                            break
                    except KeyboardInterrupt:
                        sys.exit(0)
        else:
                for i in range(1, 4):
                    msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                    clear = " " * (80 - len(msg)) 
                    print(f"\r{msg}{clear}", end="")
                    sys.stdout.flush()
                    sleep(0.5)
                data = LoadJSON()
                COOKIES = data['data']['MXH']["PINTEREST"]['auth'][str(account[1][int(account_id)-1])]
                check = Pinterest(COOKIES).GETDATA()
                if check != False:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                else:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                    data['data']['MXH']["PINTEREST"]['auth'][str(account[1][int(account_id)-1])] = ""
                    SaveJSON(data)
                    print("\r" + " " * 50 + "\r", end="")
                    while True:
                        try:
                            COOKIES = input_text("Nhập Cookies : ")
                            check = Pinterest(COOKIES).GETDATA()
                            if check != False:
                                ADD_COOKIES("PINTEREST",str(account[1][int(account_id)-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                             sys.exit(0)
        while True:
            try:
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  
                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        
        draw_full_width_box("ĐANG AUTO")
        sr.Pinterest(auth,account[1][int(account_id)-1],COOKIES,delay_min,delay_max)
    elif CHOOSE== "16":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("youtube","name")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG") 
        if check_cookies("YOUTUBE",str(account[1][int(account_id)-1])) == False:
                while True:
                    try:
                        COOKIES = input_text("Nhập Cookies : ")
                        check = YT.GETDATA(COOKIES)
                        if check != False:
                            ADD_COOKIES("YOUTUBE",str(account[1][int(account_id)-1]),COOKIES)
                            break
                    except KeyboardInterrupt:
                        sys.exit(0)
        else:
                for i in range(1, 4):
                    msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                    clear = " " * (80 - len(msg)) 
                    print(f"\r{msg}{clear}", end="")
                    sys.stdout.flush()
                    sleep(0.5)
                data = LoadJSON()
                COOKIES = data['data']['MXH']["YOUTUBE"]['auth'][str(account[1][int(account_id)-1])]
                check =YT.GETDATA(COOKIES)
                if check != False:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                else:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                    data['data']['MXH']["YOUTUBE"]['auth'][str(account[1][int(account_id)-1])] = ""
                    SaveJSON(data)
                    print("\r" + " " * 50 + "\r", end="")
                    while True:
                        try:
                            COOKIES = input_text("Nhập Cookies : ")
                            check = YT.GETDATA(COOKIES)
                            if check != False:
                                ADD_COOKIES("YOUTUBE",str(account[1][int(account_id)-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                             sys.exit(0)
        while True:
            try:
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  
                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        draw_full_width_box("ĐANG AUTO") 
        sr.Youtube(auth,account[1][int(account_id)-1],COOKIES,delay_min,delay_max)
    elif CHOOSE== "17":
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("THÔNG TIN TÀI KHOẢN")
        account = GOLIKE(auth).GET_ACC("bluesky","bluesky_username")
        if len(account[0])==0:
             warning_text("KHÔNG CÓ TÀI KHOẢN ! VUI LÒNG VÀO GOLIKE ĐỂ THÊM TÀI KHOẢN")
             sys.exit(0)
        for i in range(len(account[0])):
            FN_TEXT(i+1,f"{account[1][i]} : {account[0][i]}")
        while True:
            try:
                account_id = choose_input("NHẬP TÀI KHOẢN : ")
                if(int(account_id)>0 and int(account_id)<=len(account[1])):
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        draw_full_width_box("CONFIG") 
        if check_cookies("BLUESKY",str(account[1][int(account_id)-1])) == False:
                while True:
                    try:
                        COOKIES = input_text("Nhập Authorization BlueSky : ")
                        check = BlueSky(COOKIES).GETDATA()
                        if check != False:
                            ADD_COOKIES("BLUESKY",str(account[1][int(account_id)-1]),COOKIES)
                            break
                    except KeyboardInterrupt:
                        sys.exit(0)
        else:
                for i in range(1, 4):
                    msg = f"{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}]{Color.END} => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}" + "." * i
                    clear = " " * (80 - len(msg)) 
                    print(f"\r{msg}{clear}", end="")
                    sys.stdout.flush()
                    sleep(0.5)
                data = LoadJSON()
                COOKIES = data['data']['MXH']["BLUESKY"]['auth'][str(account[1][int(account_id)-1])]
                check =BlueSky(COOKIES).GETDATA()
                if check != False:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_GREEN}LIVE")
                else:
                    print(f"\r{Color.LIGHT_CYAN}[{Color.END}^_^{Color.LIGHT_CYAN}{Color.END}] => {Color.LIGHT_PURPLE}Đang check cookie{Color.END}...{Color.LIGHT_RED}DIE")
                    data['data']['MXH']["BLUESKY"]['auth'][str(account[1][int(account_id)-1])] = ""
                    SaveJSON(data)
                    print("\r" + " " * 50 + "\r", end="")
                    while True:
                        try:
                            COOKIES = input_text("Nhập Authorization BlueSky : ")
                            check = BlueSky(COOKIES).GETDATA()
                            if check != False:
                                ADD_COOKIES("BLUESKY",str(account[1][int(account_id)-1]),COOKIES)
                                break
                        except KeyboardInterrupt:
                             sys.exit(0)
        while True:
            try:
                delay =  input_text("Nhập Delay Nhiệm Vụ (Hoặc random khi nhập 2 số cách nhau bằng dấu ',') : ")
                if "," in delay:
                        delay = delay.split(",")
                        delay = [int(x) for x in delay]
                        if(delay[0]<delay[1] and min(delay) != 0):
                            delay_min = delay[0]
                            delay_max = delay[1]
                            break  
                else:
                    if int(delay) > 0:
                        delay_min,delay_max = int(delay), int(delay)
                        break
            except KeyboardInterrupt:
                    sys.exit(0)
            except Exception as e:
                pass
        draw_full_width_box("ĐANG AUTO") 
        sr.BlueSky(auth,account[1][int(account_id)-1],COOKIES,delay_min,delay_max)
    elif CHOOSE == "0":
        data = LoadJSON()
        data['data']['Auth'] = ""
        SaveJSON(data)
        main()
    
def main():
    os.system("cls" if os.name == "nt" else "clear")
    ascii_img()
    split_terminal()
    LOGO_TEXT("7A","1")
    LOGO_TEXT("BẢN QUYỀN","KHANG")
    split_terminal()
    draw_full_width_box("THÔNG TIN TÀI KHOẢN")
    data = LoadJSON()
    if(data['data']['Auth'] == ""):
        warning_text("Bạn chưa nhập authorization vui lòng nhập authorization ! ")
        while True:
            auth = input_text("Nhập Authorization : ")
            check = GOLIKE(auth).GET_USER()
            if check != False:
                data['data']['Auth'] = auth
                SaveJSON(data)
                break
        main()
    else:
        info = GOLIKE(data['data']['Auth']).GET_USER()
        sleep(3)
        if info != False :
            menu_live(info,data['data']['Auth'])

        else :
            data['data']['Auth'] = ""
            SaveJSON(data)
            main()
if __name__ == "__main__":
    main()

