import { Route, Routes } from "react-router-dom"
import {Navigation2, Counter, Footer} from "cmm"
import {Schedule} from "cop"
import {LoginForm, SignUp} from "uat"
import fashion from 'images/fashion.png'
import { Number } from "movie"
import { Iris, Stroke, Fashion, AiTrader } from "dlearn"
import { NaverMovie } from "webcrawler"
import { SamsungReport } from "nlp"
import UserList from "uat/containers/UserList"


const Home = () => {
    const imageSize = {width: 300, height: 300}
    return (<>
    <table style={{ width: "1200px", height: "550px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation2/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/home"></Route>
                <Route path="/counter" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/login" element={<LoginForm/>}></Route>
                <Route path="/signup" element={<SignUp/>}></Route>
                <Route path="/stroke" element={<Stroke/>}></Route>
                <Route path="/iris" element={<Iris/>}></Route>
                <Route path="/fashion" element={<Fashion/>}></Route>
                <Route path="/number" element={<Number/>}></Route>
                <Route path="/naver-movie" element={<NaverMovie/>}></Route>
                <Route path="/report-view" element={<SamsungReport/>}></Route>
                <Route path="/user-list" element={<UserList/>}></Route>
                <Route path="/aitrader" element={<AiTrader/>}></Route>
            </Routes>
            </td>
        </tr>
        <tr>
            <td>
                <img src={fashion} style={imageSize} alt="이미지"/>
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}
export default Home