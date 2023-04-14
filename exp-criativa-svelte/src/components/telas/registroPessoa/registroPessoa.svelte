<script>
    import Router, { location, link } from "svelte-spa-router";
    import Login from "../login/login.svelte";
</script>

<Router
    routes={{
        "/login": Login,
    }}
/>

<div class="conteudo">
    <div class="card">
        <div class="ttl">
            <h2>Registro</h2>
        </div>

        <div class="content">
            <div class="inputUsuario">
                <input type="text" placeholder="Usuário" />
            </div>
            <div class="inputEmail">
                <input type="email" placeholder="E-mail" />
            </div>
            <div class="inputSenha">
                <input type="password" placeholder="Senha" />
            </div>
            <div class="inputConfirmarSenha">
                <input type="password" placeholder="Confirme a senha" />
            </div>

            <button>
                <h2>
                    <a href="/#/login">Enviar</a>
                </h2>
            </button>
        </div>
    </div>
</div>

<style>
    .conteudo {
        width: 100vw;
        height: 100vh;
        background-color: #dee1e7;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .card {
        width: 30%;
        height: 80%;
        background-color: #ffffffda;
        display: flex;
        border-radius: 10px;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .ttl {
        width: 50%;
        margin-top: 10px;
        height: 10%;
        display: flex;
        justify-content: center;
        align-items: center;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        border-bottom: 1px gray solid;
    }

    .content {
        width: 50%;
        height: 90%;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        flex-direction: column;
    }

    .inputUsuario,
    .inputSenha,
    button,
    .inputEmail,
    .inputConfirmarSenha {
        width: 100%;
        height: 10%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        border-radius: 8px;
        box-shadow: 1px 1px 10px #00000030;
    }

    input {
        width: 100%;
        height: 100%;
        border: none;
        outline: none;
        background-color: transparent;
        padding-left: 20px;
    }

    button {
        border: 0;
        background-color: lightblue;
        width: 50%;
        cursor: pointer;
        font-size: 8px;
    }
</style>
