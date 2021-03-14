set gloxp=1
set add1=1
if %1 neq "" call:%~1
goto exit

:help
call s.bat sendMessage "http://megastudios.69.mu/discord/help.png"
goto:eof

:rickroll
call s.bat sendMessage https://cdn.discordapp.com/attachments/786115426697478144/820413006377910282/yt1s.com_-_Rick_Astley_Never_Gonna_Give_You_Up_4K_60_FPS_Remastered_v720P.mp4
goto:eof

:dmme
call s.bat dmauthor Hello
goto:eof

:skin
call s.bat sendMessage https://minotar.net/armor/body/%1/100.png
goto:eof

:head
call s.bat sendMessage https://minotar.net/cube/%1/100.png
:cls
cls
goto:eof

:skincc
call s.bat sendMessage http://classicube.s3.amazonaws.com/skin/%1.png?uc
goto:eof

:headcc
call s.bat sendMessage http://classicube.s3.amazonaws.com/face/%1.png?uc
goto:eof

:hug
call s.bat sendMessage "you hugged %1"
timeout 1
goto:eof
:punch
call s.bat sendMessage "You punched %1 so hard their genitals disappeared"
timeout 1
goto:eof
:kiss
call s.bat sendMessage "you gave %1 a big smooch"
timeout 1
call s.bat sendMessage %2
goto:eof
//emma commands :weary://
:sendnudes
call s.bat sendMessage "Nayfen :weary:"
goto:eof
:useggsy: 
call s.bat sendMessage "no u"
goto:eof
:balls
call s.bat sendMessage "BALLS"
goto:eof
:makeout
curl -q "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=4&count=1" > number.txt
set /p num= < number.txt
echo %num%
timeout 1
if %num%==[1] call s.bat sendMessage "only with nayfen"
if %num%==[2] call s.bat sendMessage "shutup."
if %num%==[3] call s.bat sendMessage "no."
if %num%==[4] call s.bat sendMessage "you are not seggsy enough"
if %num%==[5] call s.bat sendMessage "fine :rolling_eyes:"
if %num%==[6] call s.bat sendMessage "I don't feel like cheating on nayfen today"
goto:eof
:em
call s.bat sendMessage "Nayfen"
goto:eof
:baka:
call s.bat sendMessage "You are such a baka https://i.imgur.com/kgFp2gm.png"
goto:eof
:cheat
call s.bat sendMessage "Not you cheating on me :worried:"
goto:eof
:watchaeating
call s.bat sendMessage "Guys I’m eating a burger rn"
goto:eof
:canIhaveit
call s.bat sendMessage "Sure bestie"
goto:eof
:heybestie
call s.bat sendMessage "Hey bestie"
goto:eof
:amongus
call s.bat sendMessage "Shut. up."
goto:eof
:attract
call s.bat sendMessage "hi, I realize this might come off as a bit odd haha.. but before the whole quarantine thing I saw you around school, and you seem really cool. If you aren't interested in talking that's alright, no worries!"
goto:eof
:tits
call s.bat sendMessage "I HAVE MOMMY MILKERS"
goto:eof
:randomword
curl -q http://random-word-api.herokuapp.com/word?number=1 > number.txt
set input=number.txt
set output=number2.txt
set "substr=["

(
    FOR /F "usebackq delims=" %%G IN ("%input%") DO (
        set line=%%G
        echo. !line:%substr%=!
    )
) > "%output%"
set input=number2.txt
set output=number.txt
set "substr=]"

(
    FOR /F "usebackq delims=" %%G IN ("%input%") DO (
        set line=%%G
        echo. !line:%substr%=!
    )
) > "%output%"
set input=number.txt
set output=number2.txt
set "substr=""

(
    FOR /F "usebackq delims=" %%G IN ("%input%") DO (
        set line=%%G
        echo. !line:%substr%=!
    )
) > "%output%"
set /p num= < number2.txt
echo %num%
call s.bat sendMessage "%num%"
goto:eof
:joke
@echo off
call s.bat sendMessage "Doesn't work yet"
curl -q "http://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&format=txt" > number.txt
set /p joke= <number.txt
echo "%joke%"
call s.bat sendMessage "%num%"
goto:eof
:exit