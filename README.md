# info-night-2022

Projet de la nuit de l'info 2022 de l'équipe _Village People_ de la MIAGE de Nanterre Université.

## Architecture

Projet web avec les technos:

- [x] frontend: React
- [x] backend: FastAPI <3
- [ ] base de données: MySQL, PostgreSQL ou sqlite

## Défis choisis

1.
2.
3.
4.
5.

## Conventions

### Git

- convention de nommage de branche: \_\_\_\_
- passage par des PR pour merger sur main
- CI/CD ?

### Extension VSCode

- markdownlint
- GitHub Copilot

### pre-commit

Configuration des hooks dans .pre-commit-config.yml

#### Installation

```bash
cd info-night-2022
pip install pre-commit
pre-commit install
```

À chaque commit, des vérifications sur le code seront faites, ajoutez les changements effectués automatiquement puis effectuez de nouveau le commit

### Aspect gestion de projet

## Déploiement

Scripts Terraform pour déployer sur une VM dans le Cloud de 3DS Outscale disponibles dans le répertoire ...

### Usage

```bash
cd CD
cp terraform.tfvars.example terraform.tfvars
# Complete terraform.tfvars with your credentials
terraform init
# Check plan before applying
terraform plan
# Create volume
terraform apply
# Re-run plan to check that infrastructure is up-to-date
terraform plan
# Clean ressources
terraform destroy
```

Ensuite accéder aux services via l'adresse publique de la VM qui est affichée sur votre console après l'exécution de `terraform apply` !!
