import { useState } from "react"
import CrawlerService from "../api/api"

const NaverMovie = () => {
    const [movie, setText] = useState()

    const onClick = e => {
        e.preventDefault()
        CrawlerService.navermovieGet().then(res => {
            const json = JSON.parse(res)
            setText(json['영화'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (
    <>
        <h2> 네이버 크롤러 </h2>
        <button onClick={onClick}>네이버 영화 크롤링</button><br/>
        <p>버튼을 클릭하시면, 네이버 영화 목록이 출력됩니다.</p>
        {movie}
    </>
    )
}
export default NaverMovie