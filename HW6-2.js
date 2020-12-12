cart = window.sessionStorage;
countEl = document.querySelector("#count");
const data = cart.getItem('count');
countEl.textContent = data;
document.querySelector("#add")
	.addEventListener("click", () => {
					const countEl = document.querySelector("#count");
					const count = Number(countEl.textContent);
					countEl.textContent = count +1;
					cart.setItem('price', 300);
					cart.setItem('count', Number(countEl.textContent));
					console.log(cart);
					}
						);

document.querySelector("#remove")
	.addEventListener("click", () => {
					const data = cart.getItem('count');
					if (data!=0){
						const countEl = document.querySelector("#count");
						const count = Number(countEl.textContent);
						countEl.textContent = count -1;
						total = cart.getItem('price');
						total -= 300;
						cart.setItem('count', Number(countEl.textContent));
						console.log(cart);
					}
					}
						);

document.getElementById("checkout").addEventListener("click", () => {
	const data = cart.getItem('count');
	if (data!=0){
	var order = {"price": Number(cart.getItem('price')),
	 "count":Number(cart.getItem('count')),
	 "total":(Number(cart.getItem('price'))*Number(cart.getItem('count')))
	}
	console.log(order);
	sessionStorage.clear();
	}
}
//the actual site would send this structure to mongo or any RDB, but you wold neet to reformat it
	);