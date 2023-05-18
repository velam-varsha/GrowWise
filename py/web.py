{% extends 'layout.html' %} {% block body %}

<style>
  html body {
    background-color: rgb(206, 206, 228);
  }
</style>
<!--Form Section-->
<br /><br />
<h2 style="text-align: center; margin: 0px; color: black">
  <b>Get informed advice on fertilizer based on soil</b>
</h2>
<br />

<div
  style="
    width: 350px;
    height: 40rem;
    margin: 0px auto;
    color: black;
    border-radius: 25px;
    padding: 10px 10px;
  "
>
  <form method="POST" action="{{ url_for('fert_recommend') }}">
    <div class="form-group">
      <label for="Nitrogen" style="font-size: 17px"><b>Nitrogen</b></label>
      <input
        type="number"
        class="form-control"
        id="Nitrogen"
        name="nitrogen"
        placeholder="Enter the value (example:50)"
        style="font-weight: bold"
        required
      />
    </div>
    <div class="form-group">
      <label for="Phosphorous" style="font-size: 17px"
        ><b>Phosphorous</b></label
      >
      <input
        type="number"
        class="form-control"
        id="Phosphorous"
        name="phosphorous"
        placeholder="Enter the value (example:50)"
        style="font-weight: bold"
        required