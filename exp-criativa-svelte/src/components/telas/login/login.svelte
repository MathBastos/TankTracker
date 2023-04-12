<!-- <script>
    import Card from "../../cards/card.svelte";
</script> -->

<div class="conteudo">
    <div class="card">
        <div class="esq">
            <div class="logo">
                <h2>TankTracker</h2>
            </div>
            <div class="ttl">
                <h2>Seja bem vindo</h2>
            </div>

            <div class="content">
                <div class="inputUsuario">
                    <input type="text" placeholder="Usuário" />
                    <ion-icon class="icon" name="mail-outline" />
                </div>
                <div class="inputSenha">
                    <input type="password" placeholder="Senha" />
                    <ion-icon class="icon" name="lock-closed-outline" />
                </div>

                <button>
                    <h2>Login</h2>
                </button>

                <div class="register">
                    <h3>
                        <a href="">Crie sua conta</a>
                    </h3>
                </div>
            </div>
        </div>

        <script
            type="module"
            src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"
        ></script>
        <script
            nomodule
            src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"
        ></script>

        <div class="dir">
            <img src="images/aquario-landing-page.jpg" alt="" />
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

    @import url("https://fonts.cdnfonts.com/css/gotham");

    :global(h2, h3, ::placeholder) {
        font-family: "Gotham", sans-serif;
    }

    .card {
        width: 50%;
        height: 80%;
        background-color: #ffffffda;
        display: flex;
        border-radius: 10px;
    }

    .esq {
        box-shadow: 1px 1px 10px #00000030;
        width: 50%;
        height: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: column;
        border-radius: 10px;
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
    }

    .dir {
        width: 50%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        border-radius: 10px;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
        box-shadow: 1px 1px 10px #00000030;
    }

    .dir img {
        flex-shrink: 0;
        min-width: 100%;
        min-height: 100%;
    }

    .logo {
        width: 100%;
        height: 10%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        font-weight: 500;
    }

    .ttl {
        width: 100%;
        height: 10%;
        display: flex;
        justify-content: center;
        align-items: end;
        font-size: 15px;
    }

    .content {
        width: 50%;
        height: 65%;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        flex-direction: column;
        border-top: 1px solid gray;
    }

    .inputUsuario,
    .inputSenha,
    button {
        width: 100%;
        height: 10%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        border-radius: 8px;
        box-shadow: 1px 1px 10px #00000030;
    }

    input {
        width: 40%;
        height: 100%;
        border: none;
        outline: none;
        background-color: transparent;
    }

    .register {
        width: 100%;
        height: 10%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    a {
        text-decoration: none;
        color: royalblue;
    }

    button {
        border: 0;
        background-color: lightblue;
        width: 50%;
        cursor: pointer;
        font-size: 8px;
    }
</style>
