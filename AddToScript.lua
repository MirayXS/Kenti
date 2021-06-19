local url = ""

while wait(0.1) do
    local Check = game:HttpGet((f'https://{url}/GetStatus'), true)

    if Check == "True" then
        game.Players.LocalPlayer:Kick("Script has been Shut Down (For some time join discord.gg/Kenta for support)")
    end
end
