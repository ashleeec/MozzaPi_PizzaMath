# Calculating Catering Cost with Airtable
This Airtable app takes the inputs Pizza Order and Quantity and outputs the costs per pizza type and total ingredient (vairable) cost for a particular catering order. 

## How It's Made:

**Tech used:** Python, Javascript, Airtable

This project was made for MozzaPi, a family-owned pizza restaurant struggling to find a way to clearly and quickly see the costs for events and special catering orders. The firm uses Airtable to store catering and event details, so an Airtable integration would be the most convenient way to be able to see the event's variable costs to be able to appropriately charge the client.

The Airtable app allows you to calculate the cost of a catering order based
on what the client orders, the quantity at which they order, and the ingredient prices for each food item which is hardcoded as a dictionary. It takes the inputs Pizza Order and Quantity from an Airtable and outputs the costs per pizza type and total ingredient (vairable) cost for a particular catering order. 

## How to use:
The Javascript code can be copy and pasted into an Airtable scripting block (https://www.airtable.com/newsroom/introducing-scripting-block) and the outputs will appear in the Airtable.

The Python code can be run as a script, data can be imported via csv or some other means. Functionality is the same as the JS version.
