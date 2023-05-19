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
      />
    </div>

    <div class="form-group">
      <label for="Pottasium" style="font-size: 17px"><b>Pottasium</b></label>
      <input
        type="number"
        class="form-control"
        id="Pottasium"
        name="pottasium"
        placeholder="Enter the value (example:50)"
        style="font-weight: bold"
        required
      />
    </div>
    <!-- <div class="form-group">
      <label for="ph" style="font-size: 17px"><b>ph level</b></label>
      <input
        type="text"
        class="form-control"
        id="ph"
        name="ph"
        placeholder="Enter the value"
        style="font-weight: bold"
        required
      />
    </div> -->
    <div class="form-group">
      <label for="crop" style="font-size: 17px"
        ><b>Crop you want to grow</b></label
      >
      <select
        name="cropname"
        class="form-control"
        id="crop"
        placeholder="Select a crop"
        style="font-weight: bold"
        required
      >
        <option selected>Select crop</option>
        <option>rice</option>
        <option>maize</option>
        <option>chickpea</option>
        <option>kidneybeans</option>
        <option>pigeonpeas</option>
        <option>mothbeans</option>
        <option>mungbean</option>
        <option>blackgram</option>
        <option>lentil</option>
        <option>pomegranate</option>
        <option>banana</option>
        <option>mango</option>
        <option>grapes</option>
        <option>watermelon</option>
        <option>muskmelon</option>
        <option>apple</option>
        <option>orange</option>
        <option>papaya</option>
        <option>coconut</option>
        <option>cotton</option>
        <option>jute</option>
        <option>coffee</option>
      </select>
    </div>

    <div class="d-flex justify-content-center">
      <button
        type="submit"
        class="btn btn-info"
        style="
          color: black;
          font-weight: bold;
          width: 130px;
          height: 50px;
          border-radius: 12px;
          font-size: 21px;
        "
      >
        Predict
      </button>
    </div>
  </form>
</div>
{% endblock %}