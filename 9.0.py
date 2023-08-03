def tomar_decision_pago(cuenta):
    if cuenta < 150000:
        return "Pago en efectivo."
    elif cuenta <= 300000:
        return "Pago con el celular (dinero electrónico)."
    elif cuenta <= 600000:
        return "Pago con tarjeta de débito."
    else:
        return "Pago con tarjeta de crédito."

if __name__ == "__main__":
    try:
        cuenta = float(input("Ingrese el valor de la cuenta: "))

        decision_pago = tomar_decision_pago(cuenta)

        print(f"La decisión de pago es: {decision_pago}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
