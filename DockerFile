FROM golang:1.16

RUN mkdir /app
WORKDIR /app

RUN go get github.com/gin-gonic/gin
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/jinzhu/gorm
