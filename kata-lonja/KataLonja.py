Products = ["Vieras","Pulpo","Centollos"]
Sales = [50,100,50]
SalesOf = {"Madrid":[500,0,450], "Barcelona":[450,120,0], "Lisboa":[600,100,500]}
DistanceOf = {"Madrid":800,"Barcelona":1100,"Lisboa":600}
FixTransportCost = 5
VariableTransportCost = 2
ProductDeprecation = 0.01/100

class KataLonja():


    def __init__(self):
        pass

    def bestCityToShip(self,cities):
        revenues = self.calculateRevenues(cities)
        shortedRevenues = self.sortRevenues(revenues)

        return shortedRevenues[0][0]

    def calculateRevenues(self,cities):
        revenues = []
        for city in cities:
            revenues.append((city,self.revenueShippingTo(city)))

        return revenues

    def sortRevenues(self,revenues):
        return sorted(revenues, key=lambda revenues:revenues[1], reverse=True)

    def revenueShippingTo(self,city):
        return self.saleValue(city) - self.transportCost(city)

    def saleValue(self, city):
        value = 0
        for product in range(0,len(Sales)):
            value += Sales[product] * SalesOf[city][product]
        return value

    def transportCost(self,city):
        cost = 0
        cost += self.fixTransportCostTo(city)
        cost += self.variableTransportCostTo(city)
        cost += self.productDeprecationTo(city)

        return cost

    def fixTransportCostTo(self,city):
        return FixTransportCost

    def variableTransportCostTo(self,city):
        return DistanceOf[city] * VariableTransportCost

    def productDeprecationTo(self,city):
        return self.saleValue(city) * DistanceOf[city] * ProductDeprecation

