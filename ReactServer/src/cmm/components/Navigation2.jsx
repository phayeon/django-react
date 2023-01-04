import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Link } from "react-router-dom"

const Navigation2 = () => {
    const [value, setValue] = React.useState(0);
    return (
        <Box sx={{ margin: "auto" }}>
        <BottomNavigation
            showLabels
            value={value}
            onChange={(event, newValue) => {
            setValue(newValue);
            }}
        >
            <BottomNavigationAction label="Home" icon={<FavoriteIcon/>} component={Link} to="/home"/>
            <BottomNavigationAction label="Counter" icon={<FavoriteIcon/>} component={Link} to="/Counter"/>
            <BottomNavigationAction label="Todos" icon={<FavoriteIcon/>} component={Link} to="/todos"/>
            <BottomNavigationAction label="Signup" icon={<FavoriteIcon/>} component={Link} to="/signup"/>
            <BottomNavigationAction label="Login" icon={<FavoriteIcon/>} component={Link} to="/login"/>
            <BottomNavigationAction label="Stroke" icon={<FavoriteIcon/>} component={Link} to="/stroke"/>
            <BottomNavigationAction label="Iris" icon={<FavoriteIcon/>} component={Link} to="/iris"/>
            <BottomNavigationAction label="Fashion" icon={<FavoriteIcon/>} component={Link} to="/fashion"/>
            <BottomNavigationAction label="Number" icon={<FavoriteIcon/>} component={Link} to="/number"/>
            <BottomNavigationAction label="NaverMovie" icon={<FavoriteIcon/>} component={Link} to="/naver-movie"/>
        </BottomNavigation>
        <BottomNavigation
            showLabels
            value={value}
            onChange={(event, newValue) => {
            setValue(newValue);
            }}
        >
            <BottomNavigationAction label="Report" icon={<FavoriteIcon/>} component={Link} to="/report-view"/>
            <BottomNavigationAction label="UserList" icon={<FavoriteIcon/>} component={Link} to="/user-list"/>
            <BottomNavigationAction label="AiTrader" icon={<FavoriteIcon/>} component={Link} to="/aitrader"/>
        </BottomNavigation>
        </Box>
    );
}
export default Navigation2