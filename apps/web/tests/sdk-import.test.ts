import { Configuration, AccountApi } from "../../../packages/sdk/typescript";

const config = new Configuration({ basePath: "https://example.com" });
const api = new AccountApi(config);

// simple runtime check to ensure the SDK objects are usable
if (typeof api !== "object") {
  throw new Error("AccountApi did not instantiate correctly");
}

console.log("Loaded SDK configuration for base path", config.basePath);

