create env - conda create -n winew python=3.7 -y
activate env
conda activate wineq

created a requirement file
pip install -r requirements.txt

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m 'first commit'

git remote add origin https://github.com/Pranay-Surjagade/Wine-dvc-demo.git
git branch -M main
git push origin main