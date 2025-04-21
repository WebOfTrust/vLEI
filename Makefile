.PHONY: push-all, build, publish

VERSION=0.2.3
IMAGE_NAME=gleif/vlei

push-all:
	@docker push $(IMAGE_NAME) --all-tags

build:
	@docker buildx build --load \
		--platform=linux/amd64,linux/arm64 \
		-f container/Dockerfile \
		--tag $(IMAGE_NAME):latest \
		--tag $(IMAGE_NAME):$(VERSION) \
		.

publish:
	@docker push $(IMAGE_NAME):latest
	@docker push $(IMAGE_NAME):$(VERSION)
