const form = document.getElementById('sizePicker');

const grid = document.getElementById('pixelCanvas');

grid.style.border = 'none'; //remove grid/table style

function makeGrid(event) {

resetGrid = grid.cloneNode(false);
grid.style.backgroundColor = 'white';
grid.replaceChildren(resetGrid);

//get height and width values for table hieghit is row, width is columns 
let row = document.getElementById("inputHeight").value;
let col = document.getElementById("inputWidth").value;

//make the grid by appending tr, td to the table.
for(let r = 0; r < row; r++){
    let tr = document.createElement('tr');
    grid.appendChild(tr)
    for(let c = 0; c < col; c++){
        let td = document.createElement('td');
        td.style.border = 'solid black';
        tr.appendChild(td);
    }
}
grid.addEventListener('click',colorPixel);
event.preventDefault();
}

//add color(s) to cells
function colorPixel(event){
    const color = document.getElementById('colorPicker').value;
    event.target.style.backgroundColor = color;
}

//event -> sumbit calls makeGrid function
form.addEventListener('submit', makeGrid);

