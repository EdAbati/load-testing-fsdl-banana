.PHONY: help
.DEFAULT_GOAL := help

help: ## Get a list of all the targets, and their short descriptions
	@# source for the incantation: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

create-conda-env: ## Create a conda environment with the required packages
	conda env update --prune -f environment.yml
	echo "!!!RUN THE conda activate COMMAND ABOVE RIGHT NOW!!!"
