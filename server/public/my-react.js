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
        const listItems = this.props.page.map((car) => <SingleItem key={car['make']+car['model']} make ={car['make']} model={car['model']} avMileage={Math.round(car['mA'])} avAge={Number(car['mM'].toPrecision(3))}/>);
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
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(e){
        console.log(e.target.text);
        this.props.onPageChange(this.props.currentPage+1);

        switch(e.target.text){
            case 'Begining':
                this.props.onPageChange(0);
                break;
            case 'Previous':
                this.props.onPageChange(this.props.currentPage-1);
                break;
            case 'Next':
                this.props.onPageChange(this.props.currentPage+1);
                break;
            case 'End':
                this.props.onPageChange(this.props.pageCount-1);
                break;
        }
    }

    render(){
        return(<div className="PageControl">
            <a href='#' onClick={this.handleClick}>Begining</a> <a href='#' onClick={this.handleClick}>Previous</a> <a href='#' onClick={this.handleClick}>Next</a> <a href='#' onClick={this.handleClick}>End</a> {this.props.currentPage+1}/{this.props.pageCount}
        </div> );
    }
}

class SearchControl extends React.Component{
    constructor(props){
        super(props);
        this.handleFilterTextChange =  this.handleFilterTextChange.bind(this);
    }

    handleFilterTextChange(e){
        this.props.onFilterChange(e.target.value);

    }

    render(){
        return(<div className="inputSearch">
            <input type="text" id="search" name="search" placeholder="search.." value={this.props.filterText}
                      onChange={this.handleFilterTextChange}/>
        </div> );
    }
}

class SortControl extends React.Component{
    constructor(props){
        super(props);
        this.handleSortMileage = this.handleSortMileage.bind(this);
        this.handleSortAge = this.handleSortAge.bind(this);
        this.handleSortModel = this.handleSortModel.bind(this);
        this.handleSortMake = this.handleSortMake.bind(this);
    }

    handleSortMileage(e){
        e.preventDefault();
        this.props.onSortChange("mileage");
    }

    handleSortAge(e){
        e.preventDefault();
        this.props.onSortChange("age");
    }

    handleSortMake(e){
        e.preventDefault();
        this.props.onSortChange("make");
    }
    handleSortModel(e){
        e.preventDefault();
        this.props.onSortChange("model");
    }

    render(){
        return(<div>
            sort by: 
            <a className={this.props.sort == 'mileage'?"highlight-sort":""} href='#' onClick={this.handleSortMileage}>Mean Mileage</a>, 
            <a className={this.props.sort == "age" ? "highlight-sort":""} href='#' onClick={this.handleSortAge}>Mean Age</a>,
            <a className={this.props.sort == "model" ? "highlight-sort":""} href='#' onClick={this.handleSortModel}>Model</a>, 
            <a className={this.props.sort == "make"?"highlight-sort":""} href='#' onClick={this.handleSortMake}>Make</a>
            </div> );
    }

}

class PagedEOLControl extends React.Component{
    constructor(props){
        super(props);
        this.handlePageChange = this.handlePageChange.bind(this);
        this.handleSortChange = this.handleSortChange.bind(this);
        this.handleFilterTextChange = this.handleFilterTextChange.bind(this);
        this.state = {
            error: null,
            isLoaded:false,
            items:[],
            page:0,
            itemsPerPage:40,
            sortType:'mileage',
            filterText:"",
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

    handlePageChange(page){
        this.setState({page:page});
    }

    handleSortChange(sort){
        this.setState({sortType:sort});
        
        if(sort == 'age'){
            this.state.items.sort(function(a, b) {
                return parseFloat(a.mA) - parseFloat(b.mA);
            });
        }
        else if(sort == 'mileage'){
            this.state.items.sort(function(a, b) {
                return parseFloat(a.mM) - parseFloat(b.mM);
            });
        }
        else if(sort == 'model'){
            this.state.items.sort(function(a, b) {
                return a.model.localeCompare(b.model);
            });
        }
        else if(sort == 'make'){
            this.state.items.sort(function(a, b) {
                return a.make.localeCompare(b.make);
            });
        }
    }

    handleFilterTextChange(text){
        this.setState({filterText:text,page:0})
    }

    render(){

        var rows = [];

        if(this.state.filterText == ""){   
            rows = this.state.items;
        }
        else{
            this.state.items.forEach((car) => {
                if(car.model.toUpperCase().includes(this.state.filterText.toUpperCase()) ||
                    car.make.toUpperCase().includes(this.state.filterText.toUpperCase())){
                    rows.push(car);
                }
            });
        }

        const pageCount = Math.ceil(rows.length /  this.state.itemsPerPage);
        const si = this.state.page*40;
        const ei = si + 40;
        const page = rows.slice(si,ei);

        return(
            <div className ="my-style">
                <h1>Cars Taken Off Road</h1><br/>
                <div className="flex-container">
                    <SortControl sort={this.state.sortType} onSortChange={this.handleSortChange} />
                    <SearchControl filterText={this.state.filterText} onFilterChange={this.handleFilterTextChange}/>
                </div><br/>
                <SinglePage page={page}/>
                <PageControl pageCount={pageCount} currentPage={this.state.page} onPageChange={this.handlePageChange}/>
            </div>
        );
    }

}  
