#!/bin/bash



for tau_min in 8
do
    for tau_max in 24
    do
        for pc_alpha in .8 .7 .6 .4 .3 .2 .1 .01 .001 .0001
        do
		for alpha_level in .1 
		do
			for seed in 12348
			do
				sbatch --mail-type ALL --mail-user ssudhees@unil.ch --chdir /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/ --job-name tigramite_test --output /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/con-%j.out --error /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/logs/err-%j.err --partition cpu --nodes 1 --ntasks 1 --cpus-per-task 1 --mem 64G --time 01:00:00 --wrap "module purge; module load gcc; source ~/.bashrc ; conda activate /work/FAC/FGSE/IDYST/tbeucler/default/saranya/miniconda3/envs/unil_tigramite ;python /work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/parallel_tigramite/run_pcstable.py $tau_min $tau_max $pc_alpha $alpha_level $seed"
			done
		done
	done
    done
done
