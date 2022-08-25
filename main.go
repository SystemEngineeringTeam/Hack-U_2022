package main

import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
	"github.com/jinzhu/gorm"
)

type Favorite struct {
	gorm.Model
	Title         string
	Ingredients1  string
	Ingredients2  string
	Ingredients3  string
	Ingredients4  string
	Ingredients5  string
	Ingredients6  string
	Ingredients7  string
	Ingredients8  string
	Ingredients9  string
	Ingredients10 string
	Ingredients11 string
	Ingredients12 string
	Ingredients13 string
	Ingredients14 string
	Ingredients15 string
	Ingredients16 string
	Ingredients17 string
	Ingredients18 string
	Ingredients19 string
	Ingredients20 string
	Quantity1     string
	Quantity2     string
	Quantity3     string
	Quantity4     string
	Quantity5     string
	Quantity6     string
	Quantity7     string
	Quantity8     string
	Quantity9     string
	Quantity10    string
	Quantity11    string
	Quantity12    string
	Quantity13    string
	Quantity14    string
	Quantity15    string
	Quantity16    string
	Quantity17    string
	Quantity18    string
	Quantity19    string
	Quantity20    string
	Calorie       string
	Image         string
	Link          string
}

func main() {
	fmt.Printf("Hello World!")
	db := sqlConnect()
	db.AutoMigrate(&Favorite{})
	defer db.Close()

	router := gin.Default()
	router.LoadHTMLGlob("templates/*.html")

	//home.htmlに遷移
	router.GET("/", func(ctx *gin.Context) {
		db := sqlConnect()
		var favorites []Favorite
		db.Order("created_at asc").Find(&favorites)
		defer db.Close()

		ctx.HTML(200, "home.html", gin.H{
			"favorites": favorites,
		})
	})

	//favorites.htmlに遷移
	router.GET("/favorites/", func(ctx *gin.Context) {
		db := sqlConnect()
		var favorites []Favorite
		db.Order("created_at asc").Find(&favorites)
		defer db.Close()

		ctx.HTML(200, "favorites.html", gin.H{
			"favorites": favorites,
		})
	})

	//calculation.htmlに遷移
	router.GET("/calclator/", func(ctx *gin.Context) {
		db := sqlConnect()
		var favorites []Favorite
		db.Order("created_at asc").Find(&favorites)
		defer db.Close()

		ctx.HTML(200, "calclator.html", gin.H{
			"favorites": favorites,
		})
	})

	router.POST("/new", func(ctx *gin.Context) {
		db := sqlConnect()
		title := ctx.PostForm("title")
		ingredients1 := ctx.PostForm("ingredients1")
		ingredients2 := ctx.PostForm("ingredients2")
		ingredients3 := ctx.PostForm("ingredients3")
		ingredients4 := ctx.PostForm("ingredients4")
		ingredients5 := ctx.PostForm("ingredients5")
		ingredients6 := ctx.PostForm("ingredients6")
		ingredients7 := ctx.PostForm("ingredients7")
		ingredients8 := ctx.PostForm("ingredients8")
		ingredients9 := ctx.PostForm("ingredients9")
		ingredients10 := ctx.PostForm("ingredients10")
		ingredients11 := ctx.PostForm("ingredients11")
		ingredients12 := ctx.PostForm("ingredients12")
		ingredients13 := ctx.PostForm("ingredients13")
		ingredients14 := ctx.PostForm("ingredients14")
		ingredients15 := ctx.PostForm("ingredients15")
		ingredients16 := ctx.PostForm("ingredients16")
		ingredients17 := ctx.PostForm("ingredients17")
		ingredients18 := ctx.PostForm("ingredients18")
		ingredients19 := ctx.PostForm("ingredients19")
		ingredients20 := ctx.PostForm("ingredients20")
		quantity1 := ctx.PostForm("quantity1")
		quantity2 := ctx.PostForm("quantity2")
		quantity3 := ctx.PostForm("quantity3")
		quantity4 := ctx.PostForm("quantity4")
		quantity5 := ctx.PostForm("quantity5")
		quantity6 := ctx.PostForm("quantity6")
		quantity7 := ctx.PostForm("quantity7")
		quantity8 := ctx.PostForm("quantity8")
		quantity9 := ctx.PostForm("quantity9")
		quantity10 := ctx.PostForm("quantity10")
		quantity11 := ctx.PostForm("quantity11")
		quantity12 := ctx.PostForm("quantity12")
		quantity13 := ctx.PostForm("quantity13")
		quantity14 := ctx.PostForm("quantity14")
		quantity15 := ctx.PostForm("quantity15")
		quantity16 := ctx.PostForm("quantity16")
		quantity17 := ctx.PostForm("quantity17")
		quantity18 := ctx.PostForm("quantity18")
		quantity19 := ctx.PostForm("quantity19")
		quantity20 := ctx.PostForm("quantity20")
		calorie := ctx.PostForm("carolie")
		image := ctx.PostForm("image")
		link := ctx.PostForm("link")

		//fmt.Println("create user " + name + " with email " + email)
		db.Create(&Favorite{Title: title,
			Ingredients1: ingredients1, Ingredients2: ingredients2, Ingredients3: ingredients3, Ingredients4: ingredients4, Ingredients5: ingredients5,
			Ingredients6: ingredients6, Ingredients7: ingredients7, Ingredients8: ingredients8, Ingredients9: ingredients9, Ingredients10: ingredients10,
			Ingredients11: ingredients11, Ingredients12: ingredients12, Ingredients13: ingredients13, Ingredients14: ingredients14, Ingredients15: ingredients15,
			Ingredients16: ingredients16, Ingredients17: ingredients17, Ingredients18: ingredients18, Ingredients19: ingredients19, Ingredients20: ingredients20,
			Quantity1: quantity1, Quantity2: quantity2, Quantity3: quantity3, Quantity4: quantity4, Quantity5: quantity5,
			Quantity6: quantity6, Quantity7: quantity7, Quantity8: quantity8, Quantity9: quantity9, Quantity10: quantity10,
			Quantity11: quantity11, Quantity12: quantity12, Quantity13: quantity13, Quantity14: quantity14, Quantity15: quantity15,
			Quantity16: quantity16, Quantity17: quantity17, Quantity18: quantity18, Quantity19: quantity19, Quantity20: quantity20,
			Calorie: calorie, Image: image, Link: link})
		defer db.Close()

		ctx.Redirect(302, "/")
	})
	router.Run()
}

func sqlConnect() (database *gorm.DB) {
	DBMS := "mysql"
	USER := "go_test"
	PASS := "password"
	PROTOCOL := "tcp(db:3306)"
	DBNAME := "go_database"

	CONNECT := USER + ":" + PASS + "@" + PROTOCOL + "/" + DBNAME + "?charset=utf8&parseTime=true&loc=Asia%2FTokyo"

	count := 0
	db, err := gorm.Open(DBMS, CONNECT)
	if err != nil {
		for {
			if err == nil {
				fmt.Println("")
				break
			}
			fmt.Print(".")
			time.Sleep(time.Second)
			count++
			if count > 180 {
				fmt.Println("")
				panic(err)
			}
			db, err = gorm.Open(DBMS, CONNECT)
		}
	}

	return db
}
