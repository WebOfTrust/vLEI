.PHONY: push-all
push-all:
	@docker push gleif/vlei --all-tags

.PHONY: build-vlei
build-vlei:
	@docker buildx build --load --platform=linux/amd64 -f container/Dockerfile --tag gleif/vlei:latest --tag gleif/vlei:0.2.1 .
