up:
	docker-compose down
	docker-compose up -d
down:
	docker-compose down
ps:
	docker-compose ps
logs:
	docker-compose logs -f
build:
	docker-compsoe build
test:
	docker-compose up -d
	curl http://localhost:3000/
	curl http://localhost:3000/slow