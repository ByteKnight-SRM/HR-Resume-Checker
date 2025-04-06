const express = require("express");
const cors = require("cors");
const { CosmosClient } = require("@azure/cosmos");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

// Cosmos DB Setup
const client = new CosmosClient(process.env.COSMOS_CONNECTION_STRING);
const database = client.database("CandidatesDB");
const container = database.container("Profiles");

app.get("/candidates", async (req, res) => {
  const query = "SELECT * FROM c";
  const { resources } = await container.items.query(query).fetchAll();
  res.json(resources);
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
