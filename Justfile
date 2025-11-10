default: 
    just --list

up:
    docker compose --profile develop --file ./docker/compose.yml up scrapper-dev

down:
    docker compose --profile develop --file ./docker/compose.yml down

shell:
    docker exec -it docker-scrapper-dev-1 bash

# logs:
#     docker compose --file ./docker/compose.yml logs --follow