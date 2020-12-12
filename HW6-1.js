
var myCollection = ['http://bgfons.com/uploads/paint/paint_texture2171.jpg',
'https://image.freepik.com/free-photo/watercolor-dark-burgundy-background-painting-texture-watercolor-deep-red-pink-color-old-ovelay_145343-65.jpg',
 "https://www.publicdomainpictures.net/pictures/130000/velka/red-box-background.jpg"];

document.querySelector("#next_btn").addEventListener("click", () => {
					const countEl = document.querySelector("#image");
					const source = countEl.src;
					var a = myCollection.indexOf(source);
					if (a != myCollection.length){
					countEl.src = myCollection[a+1];
				}
					}
						);

document.querySelector("#prev_btn").addEventListener("click", () => {
					const countEl = document.querySelector("#image");
					const source = countEl.src;
					var a = myCollection.indexOf(source);
					if (a != 0){
					countEl.src = myCollection[a-1];
				}
					}
						);