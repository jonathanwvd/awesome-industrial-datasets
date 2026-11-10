# Delta Robot Parameters for Predictive Maintenance

Eleven feed-forward controller parameters read from a delta robot that picks and places barrels and springs on a pen production line in a smart factory.

- **Domain:** Robotics and automation
- **Asset / Process:** Robots and manipulators
- **Modality:** Tabular
- **Task:** Condition monitoring
- **Access:** Mendeley Data
- **Year:** 2021
- **License:** CC BY
- **Publisher:** Zurcher Hochschule fur Angewandte Wissenschaften

## Description

This Mendeley Data record from the Zurcher Hochschule fur Angewandte Wissenschaften holds parameter readings from a delta robot, contributed by Kiavash Fathi, Hans Wernher van de Venn and Marcel Honegger. The robot belongs to a smart factory, where it picks and places barrels and springs in a customised pen production line.

Eleven parameters come from the feed-forward controller and depend on the movement: motor inertia, gravity, mass, spring offset, spring constant, three Coulomb friction terms and three viscous friction terms. Each parameter has its own learning rate, listed with the data. BarrelMovement.csv covers barrel pick and place; SpringMovement_Converged.csv holds converged spring values, while SpringMovement_withTransientData.csv also keeps readings taken before the parameters settle to steady state.

The contributors advise normalising the readings so that patterns can be learned across models, and used scikit-learn for their own preprocessing. Version 1 was published in August 2021 under CC BY 4.0.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/fddp3dvvzr)
- [Industrial Atlas page](https://www.indatlas.com/datasets/delta-robot-pdm/)

[⬅️ Back to Index](../README.md)
