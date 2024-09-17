import React, {component} from "react"
import {render} from 'react-dom'

export default class App extends component {
    constructor(props) {
        super (props)
    }

    render(){
        return (<h1>Testing React Code</h1>)
    }
}

const appDiv = document.getElementById('app')
render (<App/>, appDiv)