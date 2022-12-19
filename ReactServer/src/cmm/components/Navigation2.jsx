import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Link } from "react-router-dom"

const Navigation2 = () => {
    const [value, setValue] = React.useState(0);
    return (
        <Box sx={{ width: 500 }}>
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
            <BottomNavigationAction label="Signup" icon={<FavoriteIcon/>} component={Link} Link to="/signup"/>
            <BottomNavigationAction label="Login" icon={<FavoriteIcon/>} component={Link} Link to="/login"/>
            <BottomNavigationAction label="Stroke" icon={<FavoriteIcon/>} component={Link} Link to="/stroke"/>
            <BottomNavigationAction label="Iris" icon={<FavoriteIcon/>} component={Link} Link to="/iris"/>
            <BottomNavigationAction label="Fashion" icon={<FavoriteIcon/>} component={Link} Link to="/fashion"/>
            <BottomNavigationAction label="Number" icon={<FavoriteIcon/>} component={Link} Link to="/number"/>
        </BottomNavigation>
        </Box>
    );
}
export default Navigation2