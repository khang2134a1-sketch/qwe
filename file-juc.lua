-- Create UI elements
local player = game.Players.LocalPlayer
local gui = Instance.new("ScreenGui")
gui.Name = "ScriptRunner"
gui.Parent = player:WaitForChild("PlayerGui")

-- Title label
local title = Instance.new("TextLabel")
title.Text = "Script Runner"
title.Size = UDim2.new(0, 200, 0, 40)
title.Position = UDim2.new(0.5, -100, 0.2, 0)
title.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
title.TextColor3 = Color3.fromRGB(0, 0, 0)
title.Font = Enum.Font.SourceSansBold
title.TextSize = 24
title.Parent = gui

-- Textbox for pasting script
local textbox = Instance.new("TextBox")
textbox.Text = ""
textbox.Size = UDim2.new(0, 400, 0, 150)
textbox.Position = UDim2.new(0.5, -200, 0.4, 0)
textbox.BackgroundColor3 = Color3.fromRGB(240, 240, 240)
textbox.TextColor3 = Color3.fromRGB(0, 0, 0)
textbox.TextSize = 16
textbox.MultiLine = true
textbox.Parent = gui

-- Run button
local button = Instance.new("TextButton")
button.Text = "Run Script"
button.Size = UDim2.new(0, 100, 0, 40)
button.Position = UDim2.new(0.5, -50, 0.7, 0)
button.BackgroundColor3 = Color3.fromRGB(0, 128, 255)
button.TextColor3 = Color3.fromRGB(255, 255, 255)
button.TextSize = 18
button.Parent = gui

-- Function to execute script
local function runScript()
    local scriptText = textbox.Text
    if scriptText == "" then
        warn("No script text provided")
        return
    end
    
    -- Execute the script
    local success, result = pcall(function()
        loadstring(scriptText)()
    end)
    
    if not success then
        warn("Script error:", tostring(result))
    else
        print("Script executed successfully")
    end
end

-- Connect button click to run function
button.MouseButton1Click:Connect(runScript)

-- Optional: Add keyboard shortcut (Ctrl+Enter)
local function onKeyPress(input, gameProcessed)
    if input.KeyCode == Enum.KeyCode.Enter and input.Modifiers == Enum.ModifierKey.Control then
        runScript()
    end
end
player:GetMouse().KeyDown:Connect(onKeyPress)
