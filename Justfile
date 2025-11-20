default:
    just --list

# Bring up compose for an environment (default: dev)
up ENV = "dev":
    docker compose --file ./docker/{{ENV}}/compose.yml up

# Bring down compose for an environment (default: dev)
down ENV = "dev":
    docker compose --file ./docker/{{ENV}}/compose.yml down

shell:
    docker exec -it docker-scrapper-dev-1 bash

logs ENV = "dev":
    docker compose --file ./docker/{{ENV}}/compose.yml logs --follow
