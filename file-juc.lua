-- ============================================================
-- Script Runner - Remake (Kéo thả + Thu nhỏ/Phóng to)
-- Tác giả: (Bạn)
-- Chức năng: Chạy Lua, kéo thả, thu nhỏ/phóng to cửa sổ
-- ============================================================

-- 1. Khởi tạo dịch vụ và biến toàn cục
local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local player = Players.LocalPlayer

local gui = Instance.new("ScreenGui")
gui.Name = "ScriptRunnerGUI"
gui.ResetOnSpawn = false
gui.Parent = player:WaitForChild("PlayerGui")

-- Kích thước cửa sổ
local WINDOW_WIDTH = 420
local MAX_HEIGHT = 270
local MIN_HEIGHT = 48   -- Chỉ đủ chứa thanh tiêu đề

-- Trạng thái
local isMinimized = false
local isDragging = false
local dragOffset = Vector2.new()

-- 2. Tạo Frame chính (cửa sổ)
local mainFrame = Instance.new("Frame")
mainFrame.Size = UDim2.new(0, WINDOW_WIDTH, 0, MAX_HEIGHT)
mainFrame.Position = UDim2.new(0.5, -WINDOW_WIDTH/2, 0.3, -MAX_HEIGHT/2)
mainFrame.BackgroundColor3 = Color3.fromRGB(30, 30, 40)
mainFrame.BorderSizePixel = 0
mainFrame.BackgroundTransparency = 0.1
mainFrame.ClipsDescendants = true   -- Quan trọng: giúp ẩn nội dung khi thu nhỏ
mainFrame.Parent = gui

-- Bo góc cho cửa sổ (dùng UICorner)
local corner = Instance.new("UICorner")
corner.CornerRadius = UDim.new(0, 8)
corner.Parent = mainFrame

-- 3. Thanh tiêu đề (vừa để hiển thị, vừa là vùng kéo thả)
local titleBar = Instance.new("Frame")
titleBar.Size = UDim2.new(1, 0, 0, 45)
titleBar.BackgroundTransparency = 1
titleBar.Parent = mainFrame

-- Nhãn tiêu đề
local title = Instance.new("TextLabel")
title.Text = "Discord : minhhoalong6 "
title.Size = UDim2.new(1, -80, 1, 0)
title.Position = UDim2.new(0, 10, 0, 0)
title.BackgroundTransparency = 1
title.TextColor3 = Color3.fromRGB(255, 255, 255)
title.Font = Enum.Font.GothamBold
title.TextSize = 22
title.TextXAlignment = Enum.TextXAlignment.Left
title.Parent = titleBar

-- 4. Các nút điều khiển cửa sổ (thu nhỏ / phóng to)
local minButton = Instance.new("TextButton")
minButton.Text = "─"
minButton.Size = UDim2.new(0, 30, 0, 30)
minButton.Position = UDim2.new(1, -80, 0, 8)
minButton.BackgroundColor3 = Color3.fromRGB(60, 60, 70)
minButton.TextColor3 = Color3.fromRGB(255, 255, 255)
minButton.Font = Enum.Font.Gotham
minButton.TextSize = 22
minButton.BorderSizePixel = 0
minButton.Parent = mainFrame

local closeButton = Instance.new("TextButton") -- Nút thoát hẳn (không bắt buộc, nhưng tiện)
closeButton.Text = "✕"
closeButton.Size = UDim2.new(0, 30, 0, 30)
closeButton.Position = UDim2.new(1, -40, 0, 8)
closeButton.BackgroundColor3 = Color3.fromRGB(200, 60, 60)
closeButton.TextColor3 = Color3.fromRGB(255, 255, 255)
closeButton.Font = Enum.Font.Gotham
closeButton.TextSize = 18
closeButton.BorderSizePixel = 0
closeButton.Parent = mainFrame

-- 5. Vùng nhập script (TextBox)
local textbox = Instance.new("TextBox")
textbox.Text = ""
textbox.Size = UDim2.new(1, -20, 0, 160)
textbox.Position = UDim2.new(0, 10, 0, 55)
textbox.BackgroundColor3 = Color3.fromRGB(20, 20, 30)
textbox.TextColor3 = Color3.fromRGB(220, 220, 220)
textbox.Font = Enum.Font.Code
textbox.TextSize = 15
textbox.MultiLine = true
textbox.ClearTextOnFocus = false
textbox.PlaceholderText = "Dán script Lua của bạn vào đây..."
textbox.BackgroundTransparency = 0.2
textbox.Parent = mainFrame

-- 6. Hàng nút lệnh (Run + Clear + Status)
local buttonContainer = Instance.new("Frame")
buttonContainer.Size = UDim2.new(1, -20, 0, 40)
buttonContainer.Position = UDim2.new(0, 10, 0, 225)
buttonContainer.BackgroundTransparency = 1
buttonContainer.Parent = mainFrame

-- Nút Run
local runButton = Instance.new("TextButton")
runButton.Text = "▶ Run"
runButton.Size = UDim2.new(0, 100, 0, 36)
runButton.Position = UDim2.new(0, 0, 0, 2)
runButton.BackgroundColor3 = Color3.fromRGB(0, 180, 80)
runButton.TextColor3 = Color3.fromRGB(255, 255, 255)
runButton.Font = Enum.Font.GothamSemibold
runButton.TextSize = 18
runButton.BorderSizePixel = 0
runButton.Parent = buttonContainer

-- Nút Clear
local clearButton = Instance.new("TextButton")
clearButton.Text = "✕ Clear"
clearButton.Size = UDim2.new(0, 80, 0, 36)
clearButton.Position = UDim2.new(0, 110, 0, 2)
clearButton.BackgroundColor3 = Color3.fromRGB(200, 60, 60)
clearButton.TextColor3 = Color3.fromRGB(255, 255, 255)
clearButton.Font = Enum.Font.GothamSemibold
clearButton.TextSize = 18
clearButton.BorderSizePixel = 0
clearButton.Parent = buttonContainer

-- Label trạng thái
local statusLabel = Instance.new("TextLabel")
statusLabel.Text = "Ready"
statusLabel.Size = UDim2.new(0, 180, 0, 30)
statusLabel.Position = UDim2.new(1, -190, 0, 5)
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.fromRGB(150, 200, 255)
statusLabel.Font = Enum.Font.Gotham
statusLabel.TextSize = 14
statusLabel.TextXAlignment = Enum.TextXAlignment.Right
statusLabel.Parent = buttonContainer

-- 7. Hàm thực thi script (giữ nguyên)
local function executeScript()
    local code = textbox.Text
    if code == "" or code:match("^%s*$") then
        statusLabel.Text = "⚠️ Chưa có script"
        statusLabel.TextColor3 = Color3.fromRGB(255, 200, 100)
        return
    end

    statusLabel.Text = "⏳ Đang chạy..."
    statusLabel.TextColor3 = Color3.fromRGB(100, 200, 255)
    
    local success, err = pcall(function()
        local fn = loadstring(code)
        if not fn then error("Lỗi cú pháp: loadstring trả về nil") end
        fn()
    end)

    if success then
        statusLabel.Text = "✅ Thực thi thành công!"
        statusLabel.TextColor3 = Color3.fromRGB(100, 255, 150)
    else
        local errMsg = tostring(err):sub(1, 60)
        statusLabel.Text = "❌ Lỗi: " .. errMsg
        statusLabel.TextColor3 = Color3.fromRGB(255, 100, 100)
        warn("Lỗi script: ", err)
    end
end

-- 8. Chức năng thu nhỏ / phóng to
local function toggleMinimize()
    isMinimized = not isMinimized
    
    if isMinimized then
        mainFrame.Size = UDim2.new(0, WINDOW_WIDTH, 0, MIN_HEIGHT)
        textbox.Visible = false
        buttonContainer.Visible = false
        minButton.Text = "➕"  -- Đổi thành dấu cộng để báo hiệu phóng to
    else
        mainFrame.Size = UDim2.new(0, WINDOW_WIDTH, 0, MAX_HEIGHT)
        textbox.Visible = true
        buttonContainer.Visible = true
        minButton.Text = "─"
    end
end

minButton.MouseButton1Click:Connect(toggleMinimize)

-- Nút Close (thoát hẳn GUI)
closeButton.MouseButton1Click:Connect(function()
    gui:Destroy()
end)

-- 9. Chức năng kéo thả cửa sổ (bắt sự kiện toàn cục)
local function isMouseOverTitleBar()
    local mousePos = UserInputService:GetMouseLocation()
    local framePos = mainFrame.AbsolutePosition
    local frameSize = mainFrame.AbsoluteSize
    
    -- Vùng kéo là 45px trên cùng của Frame (thanh tiêu đề)
    if mousePos.X >= framePos.X and mousePos.X <= framePos.X + frameSize.X and
       mousePos.Y >= framePos.Y and mousePos.Y <= framePos.Y + 45 then
        return true
    end
    return false
end

local function onInputBegan(input, gameProcessed)
    if gameProcessed then return end
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        if isMouseOverTitleBar() then
            isDragging = true
            local mousePos = UserInputService:GetMouseLocation()
            dragOffset = mousePos - mainFrame.AbsolutePosition
        end
    end
end

local function onInputChanged(input, gameProcessed)
    if gameProcessed then return end
    if input.UserInputType == Enum.UserInputType.MouseMovement and isDragging then
        local mousePos = UserInputService:GetMouseLocation()
        local newX = mousePos.X - dragOffset.X
        local newY = mousePos.Y - dragOffset.Y
        mainFrame.Position = UDim2.new(0, newX, 0, newY)
    end
end

local function onInputEnded(input, gameProcessed)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        isDragging = false
    end
end

UserInputService.InputBegan:Connect(onInputBegan)
UserInputService.InputChanged:Connect(onInputChanged)
UserInputService.InputEnded:Connect(onInputEnded)

-- 10. Gán sự kiện cho các nút Run / Clear
runButton.MouseButton1Click:Connect(executeScript)
clearButton.MouseButton1Click:Connect(function()
    textbox.Text = ""
    statusLabel.Text = "🧹 Đã xoá"
    statusLabel.TextColor3 = Color3.fromRGB(200, 200, 200)
end)

-- 11. Phím tắt Ctrl + Enter (dùng UserInputService mới)
local function onKeyDown(input, gameProcessed)
    if not gameProcessed and input.KeyCode == Enum.KeyCode.Return and input.Modifiers == Enum.ModifierKey.Control then
        executeScript()
    end
end
UserInputService.InputBegan:Connect(onKeyDown)

-- 12. Hiệu ứng hover cho nút
local function setupHover(btn)
    local orig = btn.BackgroundColor3
    btn.MouseEnter:Connect(function() 
        btn.BackgroundColor3 = orig:Lerp(Color3.new(1,1,1), 0.15) 
    end)
    btn.MouseLeave:Connect(function() 
        btn.BackgroundColor3 = orig 
    end)
end
setupHover(runButton)
setupHover(clearButton)
setupHover(minButton)
setupHover(closeButton)

print("🚀 Script Runner đã sẵn sàng! Kéo thả tiêu đề để di chuyển, nhấn ─ để thu nhỏ.")
