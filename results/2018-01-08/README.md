# Hyperparametrized training of model `blablabl` on seqlen = 100..1000

* Started: 2021-02-16, 2021-03-02, queued 2021-03-19
* System: Vera
* Commit: `9aa6895b`
* Log: `slurm-1962506.out`, `slurm-1984673.out`, `slurm-2018053.out`
* Time taken: 168:00 + 55:00 + 

```shell
sbatch -A C3SE2021-1-18 -t 168:00:00 --gres=gpu:V100:2 \
  run_python.sh results/2018-01-08/model.py  
```

Best config with mean_loss = [...]


# 


