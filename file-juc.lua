-- ============================================================
-- Script Runner - Remake theo phong cách minhhoalong
-- Tác giả: (Bạn)
-- Chức năng: Cho phép nhập và thực thi mã Lua trong Roblox
-- ============================================================

-- 1. Khởi tạo các đối tượng cơ bản
local Players = game:GetService("Players")
local player = Players.LocalPlayer

-- Tạo GUI chính, đặt trong PlayerGui
local gui = Instance.new("ScreenGui")
gui.Name = "ScriptRunnerGUI"
gui.ResetOnSpawn = false          -- Giữ lại khi respawn
gui.Parent = player:WaitForChild("PlayerGui")

-- Hàm tạo một frame để làm khung nền (giúp giao diện gọn gàng)
local function createFrame()
    local frame = Instance.new("Frame")
    frame.Size = UDim2.new(0, 420, 0, 270)
    frame.Position = UDim2.new(0.5, -210, 0.3, -135)
    frame.BackgroundColor3 = Color3.fromRGB(30, 30, 40)
    frame.BorderSizePixel = 0
    frame.BackgroundTransparency = 0.9   -- hiệu ứng mờ
    frame.Parent = gui
    return frame
end

local mainFrame = createFrame()

-- 2. Tiêu đề (có thể kéo thả nếu muốn, nhưng giữ đơn giản)
local title = Instance.new("TextLabel")
title.Text = "🚀 Script Runner by minhhoalong6 "
title.Text = "Discord : minhhoalong6 "
title.Size = UDim2.new(1, -20, 0, 45)
title.Position = UDim2.new(0, 10, 0, 5)
title.BackgroundTransparency = 1
title.TextColor3 = Color3.fromRGB(255, 255, 255)
title.Font = Enum.Font.GothamBold
title.TextSize = 26
title.TextXAlignment = Enum.TextXAlignment.Left
title.Parent = mainFrame

-- 3. Vùng nhập script (TextBox)
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
textbox.PlaceholderText = "Paste your Lua script here..."
textbox.Parent = mainFrame

-- Bo góc cho textbox (Roblox hỗ trợ UIGradient hoặc góc riêng)
textbox.BackgroundTransparency = 0.2

-- 4. Hàng nút lệnh (Run + Clear)
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

-- Nút Clear (xoá nội dung)
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

-- Nhãn thông báo trạng thái (hiển thị kết quả hoặc lỗi)
local statusLabel = Instance.new("TextLabel")
statusLabel.Text = "Ready"
statusLabel.Size = UDim2.new(0, 180, 0, 30)
statusLabel.Position = UDim2.new(1, -190, 0, 5)  -- bên phải
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.fromRGB(150, 200, 255)
statusLabel.Font = Enum.Font.Gotham
statusLabel.TextSize = 14
statusLabel.TextXAlignment = Enum.TextXAlignment.Right
statusLabel.Parent = buttonContainer

-- 5. Hàm thực thi script chính (có hiển thị lỗi trên GUI)
local function executeScript()
    local code = textbox.Text
    if code == "" or code:match("^%s*$") then
        statusLabel.Text = "⚠️ No script entered"
        statusLabel.TextColor3 = Color3.fromRGB(255, 200, 100)
        return
    end

    statusLabel.Text = "⏳ Running..."
    statusLabel.TextColor3 = Color3.fromRGB(100, 200, 255)
    
    local success, err = pcall(function()
        local fn = loadstring(code)
        if not fn then
            error("Invalid syntax: loadstring returned nil")
        end
        fn()
    end)

    if success then
        statusLabel.Text = "✅ Executed successfully!"
        statusLabel.TextColor3 = Color3.fromRGB(100, 255, 150)
    else
        -- Hiển thị lỗi rút gọn (tránh quá dài)
        local errMsg = tostring(err):sub(1, 60)
        statusLabel.Text = "❌ Error: " .. errMsg
        statusLabel.TextColor3 = Color3.fromRGB(255, 100, 100)
        warn("Script execution error: ", err)
    end
end

-- 6. Gán sự kiện cho các nút
runButton.MouseButton1Click:Connect(executeScript)

clearButton.MouseButton1Click:Connect(function()
    textbox.Text = ""
    statusLabel.Text = "🧹 Cleared"
    statusLabel.TextColor3 = Color3.fromRGB(200, 200, 200)
end)

-- 7. Phím tắt: Ctrl + Enter
local function onKeyDown(input, gameProcessed)
    -- gameProcessed là true nếu game đã xử lý phím (tránh xung đột)
    if not gameProcessed and input.KeyCode == Enum.KeyCode.Return and input.Modifiers == Enum.ModifierKey.Control then
        executeScript()
    end
end

local userInputService = game:GetService("UserInputService")
userInputService.InputBegan:Connect(onKeyDown)

-- 8. (Tuỳ chọn) Thêm hiệu ứng hover cho nút
local function setupButtonHover(btn)
    local originalColor = btn.BackgroundColor3
    btn.MouseEnter:Connect(function()
        btn.BackgroundColor3 = originalColor:Lerp(Color3.new(1,1,1), 0.15)
    end)
    btn.MouseLeave:Connect(function()
        btn.BackgroundColor3 = originalColor
    end)
end
setupButtonHover(runButton)
setupButtonHover(clearButton)

print("Script Runner loaded. Paste your code and press Run or Ctrl+Enter.")
