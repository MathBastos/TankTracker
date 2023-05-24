window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
    const billings = document.getElementById('billing');
    if (billings) {
        fetch("/admin/billing/list_data_table").then(
            response => response.json()
        ).then(
            data => {
                if (!data.length) {
                    return
                }
                new window.simpleDatatables.DataTable(billings, {
                    data: {
                        headings: ["ID", "Valor", "Data", "Forma de Pagamento"],
                        data: data.map(item => [item["ID"], item["Valor"], item["Data"], item["Forma de Pagamento"]])
                    }
                })
            }
        )
    }
    const billingsForms = document.getElementById('billingForm');
    if (billingsForms) {
        fetch("/admin/billing/form/list_data_table").then(
            response => response.json()
        ).then(
            data => {
                if (!data.length) {
                    return
                }
                new window.simpleDatatables.DataTable(billingsForms, {
                    data: {
                        headings: ["ID", "Nome", "Descrição"],
                        data: data.map(item => [item["ID"], item["Nome"], item["Descrição"]])
                    }
                })
            }
        )
    }
});