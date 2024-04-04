# Need a conda environment, maybe a bit back-dated...

# start with sqlalchemy 1.2

conda create -n github_stats python=3.6 sqlalchemy=1.2
conda activate github_stats
pip install pandas
pip install jupyter
pip install requests
pip install psycopg2-binary
pip install matplotlib
pip install seaborn