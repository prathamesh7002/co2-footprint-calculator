from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import Co2_Form
from .models import CO2_footprint
 
def index(request):
    form = Co2_Form()
    return render(request, 'index.html', {'form': form})

def submit_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        electricity = request.POST.get("electricity")
        travel = request.POST.get("travel")
        elctronics_devices = request.POST.get("elctronics_devices")
        food_habbit = request.POST.get("food_habbit")
        water = request.POST.get("water")
        waste = request.POST.get("waste")

        # Handle missing inputs
        if not all([name, electricity, travel, elctronics_devices, food_habbit, water, waste]):
            return HttpResponse("⚠️ All fields are required. Please fill out the form completely.")

        # Convert to float for calculation
        electricity = float(electricity)
        travel = float(travel)
        elctronics_devices = float(elctronics_devices)
        water = float(water)
        waste = float(waste)

        # Calculate CO2 footprint
        co2_electricity = electricity * 0.92
        co2_travel = travel * 0.21
        co2_electronics = elctronics_devices * 0.05
        co2_water = water * 0.001
        co2_waste = waste * 0.75
        co2_food = 6 if food_habbit.lower() == "nonveg" else 4 if food_habbit.lower() == "veg" else 5

        total_co2 = co2_electricity + co2_travel + co2_electronics + co2_water + co2_waste + co2_food
        yearly_co2 =  total_co2 *365
        new_user = CO2_footprint(
            name=name,
            electricity=electricity,
            travel=travel,
            electronics_devices=elctronics_devices,
            food_habbit=food_habbit,
            water=water,
            waste=waste,
            daily_co2_emission=total_co2,
            yearly_co2_emission=yearly_co2
        )
        new_user.save()
        result = f"""
        <h2>CO₂ Footprint Report for {name}</h2>
        <ul>
            <li>Electricity CO₂: {co2_electricity:.2f} kg</li>
            <li>Travel CO₂: {co2_travel:.2f} kg</li>
            <li>Electronics CO₂: {co2_electronics:.2f} kg</li>
            <li>Water CO₂: {co2_water:.2f} kg</li>
            <li>Waste CO₂: {co2_waste:.2f} kg</li>
            <li>Food Habit CO₂: {co2_food:.2f} kg</li>
        </ul>
        <h3>Total CO₂/year Emission: <strong>{total_co2:.2f} kg/day</strong></h3>
        <h3>total CO₂/Year Emission: <strong>{yearly_co2:.2f} kg/year</strong></h3>
        """
        return HttpResponse(result)

    return HttpResponse("Invalid request method.")
