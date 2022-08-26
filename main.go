package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
	"github.com/jinzhu/gorm"
)

type Cooking struct {
	Title       string      `json:"title"`
	Ingredients Ingredients `json:"ingredients"`
	Quantities  Quantities  `json:"quantities"`
	Calorie     int         `json:"calorie"`
	Image       string      `json:"image"`
	Link        string      `json:"link"`
}

type Ingredients struct {
	Num0  string `json:"0"`
	Num1  string `json:"1"`
	Num2  string `json:"2"`
	Num3  string `json:"3"`
	Num4  string `json:"4"`
	Num5  string `json:"5"`
	Num6  string `json:"6"`
	Num7  string `json:"7"`
	Num8  string `json:"8"`
	Num9  string `json:"9"`
	Num10 string `json:"10"`
}

type Quantities struct {
	Num0  string `json:"0"`
	Num1  string `json:"1"`
	Num2  string `json:"2"`
	Num3  string `json:"3"`
	Num4  string `json:"4"`
	Num5  string `json:"5"`
	Num6  string `json:"6"`
	Num7  string `json:"7"`
	Num8  string `json:"8"`
	Num9  string `json:"9"`
	Num10 string `json:"10"`
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
		//多言語json
		json_lang_file, err := ioutil.ReadFile("json/sample.json")
		if err != nil {
			log.Println("ReadError: ", err)
			os.Exit(1)
		}

		var cooking []Cooking
		json.Unmarshal(json_lang_file, &cooking)

		ctx.HTML(200, "home.html", gin.H{
			"cooking": cooking,
		})
	})

	//favorites.htmlに遷移
	router.GET("/favorites/", func(ctx *gin.Context) {
		db := sqlConnect()
		var favorites []Favorite
		db.Find(&favorites)
		defer db.Close()

		ctx.HTML(200, "favorites.html", gin.H{
			"favorites": favorites,
		})
	})

	//calculation.htmlに遷移
	router.GET("/calclator/", func(ctx *gin.Context) {
		db := sqlConnect()
		var favorites []Favorite
		db.Find(&favorites)
		defer db.Close()

		ctx.HTML(200, "calclator.html", gin.H{
			"favorites": favorites,
		})
	})

	router.POST("/delete/:id", func(ctx *gin.Context) {
		db := sqlConnect()
		n := ctx.Param("id")
		id, err := strconv.Atoi(n)
		if err != nil {
			panic("id is not a number")
		}
		var favorites Favorite
		db.First(&favorites, id)
		db.Delete(&favorites)
		defer db.Close()

		ctx.Redirect(302, "/favorites/")
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
		quantities1 := ctx.PostForm("quantities1")
		quantities2 := ctx.PostForm("quantities2")
		quantities3 := ctx.PostForm("quantities3")
		quantities4 := ctx.PostForm("quantities4")
		quantities5 := ctx.PostForm("quantities5")
		quantities6 := ctx.PostForm("quantities6")
		quantities7 := ctx.PostForm("quantities7")
		quantities8 := ctx.PostForm("quantities8")
		quantities9 := ctx.PostForm("quantities9")
		quantities10 := ctx.PostForm("quantities10")
		calorie := ctx.PostForm("carolie")
		image := ctx.PostForm("image")
		link := ctx.PostForm("link")

		//fmt.Println("create user " + name + " with email " + email)
		db.Create(&Favorite{Title: title,
			Ingredients1: ingredients1, Ingredients2: ingredients2, Ingredients3: ingredients3, Ingredients4: ingredients4, Ingredients5: ingredients5,
			Ingredients6: ingredients6, Ingredients7: ingredients7, Ingredients8: ingredients8, Ingredients9: ingredients9, Ingredients10: ingredients10,
			Quantities1: quantities1, Quantities2: quantities2, Quantities3: quantities3, Quantities4: quantities4, Quantities5: quantities5,
			Quantities6: quantities6, Quantities7: quantities7, Quantities8: quantities8, Quantities9: quantities9, Quantities10: quantities10,
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
	Quantities1   string
	Quantities2   string
	Quantities3   string
	Quantities4   string
	Quantities5   string
	Quantities6   string
	Quantities7   string
	Quantities8   string
	Quantities9   string
	Quantities10  string
	Calorie       string
	Image         string
	Link          string
}
