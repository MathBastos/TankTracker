window.addEventListener('DOMContentLoaded', event => {
    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
    const usuarios = document.getElementById('usuarios');
    if (usuarios) {
        fetch("/usuario/lista").then(
            response => response.json()
        ).then(
            data => {
                if (!data.length) {
                    return
                }
                new window.simpleDatatables.DataTable(usuarios, {
                    data: {
                        headings: ["ID", "Nome", "Email", "Usuario", "", ""],
                        data: data.map(item => [item["ID"], item["Nome"], item["Email"], item["Usuario"], `<a href="/usuario/editar/${item["ID"]}">Editar</a>`, `<a href="/usuario/deletar/${item["ID"]}">Deletar</a>`])
                    }
                })
            }
        )
    }
    const aquarios = document.getElementById('aquarios');
    if (aquarios) {
        fetch("/aquario/lista").then(
            response => response.json()
        ).then(
            data => {
                if (!data.length) {
                    return
                }
                new window.simpleDatatables.DataTable(aquarios, {
                    data: {
                        headings: ["ID", "Nome", "Tamanho", "Quantidade de Peixes", "", ""],
                        data: data.map(item => [item["ID"], item["Nome"], item["Tamanho"], item["Quantidade de Peixes"], `<a href="/aquario/editar/${item["ID"]}">Editar</a>`, `<a href="/aquario/deletar/${item["ID"]}">Deletar</a>`])
                    }
                })
            }
        )
    }
});