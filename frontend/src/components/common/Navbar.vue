<template>
  <nav class="navbar is-fixed-top is-primary" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <h1 class="has-text-white is-size-3">mDoc</h1>
        <!--            <img src="{% static 'images/logo.png' %}" alt="mDocロゴ" /> -->
      </a>
      <a role="button" class="navbar-burger burger" data-target="navbar-menu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="navbar-menu" class="navbar-menu">
      <div class="navbar-start"></div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a href="/logout/" class="button is-light">ログアウト</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
