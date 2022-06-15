.PHONY: push-all
push-all:
	@docker push gleif/vlei --all-tags

.PHONY: build-vlei
build-vlei:
	@docker buildx build --platform=linux/amd64 --no-cache -f container/Dockerfile --tag gleif/vlei:latest --tag gleif/vlei:0.1.0 .
