import { useState } from "react"
import CrawlerService from "../api"

const NaverMovie = () => {
    const [movie, setText] = useState('')
    const [inputs, setInputs] = useState({})
    const [positive, setPositive] = useState('')
    const {review_text} = inputs

    const onClick = e => {
        e.preventDefault()
        CrawlerService.navermovieGet().then(res => {
            const json = JSON.parse(res)
            setText(json['영화'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const reviewClick = e => {
        e.preventDefault()
        CrawlerService.movieReviewPost(review_text).then(res => {
            const json = JSON.parse(res)
            setPositive(json['긍정률'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (
    <>
    
        <h2> 네이버 크롤러 </h2>
        <button onClick={onClick}>네이버 영화 크롤링</button><br/>
        <p>버튼을 클릭하시면, 네이버 영화 목록이 출력됩니다.</p>
        {movie && 
            <div>{movie}</div>
        } 
        <br/><h2> 영화 리뷰 판별기 </h2>
        <input type="text" className="box" name="review_text" placeholder="리뷰 작성" onChange={onChange}/>
        <button type="submit" onClick={reviewClick}>결과 보기</button><br/>
        <p>버튼을 클릭하시면, 리뷰의 긍정도가 판별됩니다.</p>
        {positive && 
            <div>{Math.floor(positive*100, 3)} %</div>
        } 
    </>
    )
}
export default NaverMovie