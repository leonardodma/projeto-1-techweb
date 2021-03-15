// Código para deletar card 
function deleteCard(id) {
  // Mandar enviar o form com nome deleteCard{id}
	document.getElementsByName('deleteCard' + id)[0].submit()
}

// Código para editar card
function editCard(id) {
  // Atualizar os valores dos botões 
  document.getElementsByName('button')[0].innerText = 'Completar Edição'

  // Mandar um Post com o ID do Cartão que o usuário clicou para editar.
  document.getElementsByName('ID')[0].value = id
  document.getElementsByName('titulo')[0].value = document.getElementsByName('title' + id)[0].innerText
	document.getElementsByName('detalhes')[0].value = document.getElementsByName('content' + id)[0].innerText
}


// Código do botão de Editar



// Código do Professor para Rotação dos Cards
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});
