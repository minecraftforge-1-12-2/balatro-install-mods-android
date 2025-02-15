rmdir /S /Q game
mkdir game

xcopy /E /Y "./Mods/lovely/dump" "./game"
xcopy /E /Y "./Mods" "./game/Mods/*"

copy "./lovely.lua" "./game"
copy "./nativefs.lua" "./game"
copy "./json.lua" "./game"


python copypatches.py

xcopy /E /Y "./1" "./game"
xcopy /E /Y "./2" "./game"
xcopy /E /Y "./3" "./game"
copy "./settings.jkr" "./game"


adb devices

adb shell "rm -rf /sdcard/Android/data/com.unofficial.balatro/files/save/game"

adb push "./game" "/sdcard/Android/data/com.unofficial.balatro/files/save/"