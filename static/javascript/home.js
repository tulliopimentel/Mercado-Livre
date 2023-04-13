function opinioesProduto(elementId) {
    const inputValor = document.getElementById(elementId).value;
    console.log(inputValor)
    fetch(`/opinioes/produto/${inputValor}`)
      .then(response => {
        console.log("entrou no fetch")
        // faça algo com a resposta da chamada, como exibir no console
        console.log(response);
      })
      .catch(error => {
        // trate o erro caso ocorra
        console.error(error);
      });
  }