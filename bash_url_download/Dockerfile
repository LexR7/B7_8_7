FROM alpine:3.15.0 as builder
RUN apk add --no-cache wget && apk add --no-cache ca-certificates
FROM scratch
COPY --from=builder /usr/lib/libidn2.so.0 /usr/lib/
COPY --from=builder /lib/libssl.so.1.1 /lib/
COPY --from=builder /lib/libcrypto.so.1.1 /lib/
COPY --from=builder /lib/ld-musl-aarch64.so.1 /lib/
COPY --from=builder /usr/lib/libunistring.so.2 /lib/
COPY --from=builder /usr/bin/wget /bin/sh /bin/ls /bin/
WORKDIR /home/test
CMD /bin/wget -O ${url}_favicon.ico --no-check-certificate ${url}/favicon.ico
