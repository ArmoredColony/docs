rmdir /s /q docs
sphinx-build -b html source docs
git add docs
git commit -m "Update documentation"
git push origin master

echo.
pause