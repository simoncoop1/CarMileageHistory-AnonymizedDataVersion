class MyComponent extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return (<h1>OK</h1>);
    }
}


class SingleItem extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        const ITEM = ["a make","a model","a mean age","a mean mileage" ];
        return (
            <tr>
            <td>{this.props.make}</td>
            <td>{this.props.model}</td>
            <td>{this.props.avMileage}</td>
            <td>{this.props.avAge}</td>
            </tr>
        );
    }
}

class SinglePage extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        const listItems = this.props.page.map((car) => <SingleItem key={car['make']+car['model']} make ={car['make']} model={car['model']} avMileage="22" avAge="22"/>);
        return(
            <table className="my-table">
                <thead>
                    <tr className="my-tr">
                        <th className="my-th">Make</th>
                        <th className="my-th">Model</th>
                        <th className="my-th">Mean Age (Years)</th>
                        <th className="my-th">Mean Mileage (Miles)</th>
                    </tr>
                </thead>
                <tbody>
                    {listItems}
                </tbody>
            </table>
        );

    }
}

class PageControl extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return(<div className="PageControl">
            Begining Previous Next End
        </div> );
    }

}

class SortControl extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return(<div>
            sort by: Mean Mileage, Mean Age, Model, Make
        </div> );
    }

}

class PagedEOLControl extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded:false,
            items:[],
            page:1,
            itemsPerPage:40,
        };
    }

    componentDidMount(){
        fetch("off-road-by-make-40-react.json")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result,
                    });
                    console.log(result.length);
                    
                },
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )

    }

    render(){
        //const page = [['VW','Golf','11','55'],['Ford','Focus','10','56']];

        const page = this.state.items.slice(0,40);


        

        return(
            <div className ="my-style">
                <h1>Cars Taken Off Road</h1><br/>
                {String(this.state.isLoaded)}<br/>
                <SortControl/><br/>
                <SinglePage page={page}/>
                <PageControl/>
            </div>
        );
    }

}
