# Generate new requirements.txt and dev-requirements.txt on run.
set_requirements:
	@echo ... exporting requirements.
	@pipenv update
	@pipenv lock --requirements
	@pipenv lock --requirements --dev-only
	@echo ... pipenv locked and requirements exported.