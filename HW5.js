var tbl = document.createElement('my-table')

function appendRow(arr) {
    var tbl = document.getElementById('my-table'), 
        row = tbl.insertRow(8),      
    // insert table cells to the new row
    arr.forEach (index, value) {
    	switch(index){
    		case index % 2 == 0: 
        		createCell(row.insertCell(index), value, 'row');
        	case index % 2 != 0: 
        		createCell(row.insertCell(index), value, 'row');
    	}
    }
}
 
function createCell(cell, text, style) {
    var div = document.createElement('div'),
        txt = document.createTextNode(text); 
    div.appendChild(txt);                    
    div.setAttribute('class', style);        
    div.setAttribute('className', style);    
    cell.appendChild(div);                   
}






function form(){
	var pawns = ["П", "П", "П", "П", "П", "П", "П", "П"]];
	var full = ["Л", "К", "Ф", "Король", "королева", "Ф", "К", "Л"]];
	var empty = ["", "", "", "", "", "", "", ""]];
	appendRow(full);
	appendRow(pawns);
	for (i=0, i>4, i++){
		appendRow(empty);
	}
	appendRow(pawns);
	appendRow(full);
}