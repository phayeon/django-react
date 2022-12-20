import CrawlerService from "../api/api"

const NaverMovie = () => {

    const onClick = e => {
        e.preventDefault()
        CrawlerService.navermovieGet()
        alert("크롤러 버튼 클릭")
    }
    return (
    <>
        <h2> 네이버 크롤러 </h2>
        <button onClick={onClick}>네이버 영화 크롤링</button><br/>
        <p>버튼을 클릭하시면, 네이버 영화 목록이 출력됩니다.</p>
    </>
    )
}
export default NaverMovie